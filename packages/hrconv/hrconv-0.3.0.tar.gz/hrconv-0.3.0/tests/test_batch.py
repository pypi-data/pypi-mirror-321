import mne, hrconv, os, mne_nirs
from glob import glob
from itertools import compress
from nilearn.plotting import plot_design_matrix
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from mne_nirs.channels import get_long_channels, get_short_channels, picks_pair_to_idx
from mne_nirs.experimental_design import make_first_level_design_matrix
from mne_nirs.statistics import run_glm
from mne_nirs.io import write_raw_snirf

def load(bids_dir, ex_subs = [], count = None):
    # make a list where all of the scans will get loaded into
    subject_ids = []
    raw_scans = []
    preproc_scans = []

    # Load in master file with scan order info
    subject_dirs = glob(f'{bids_dir}*/')
    if count:
        subject_dirs = subject_dirs[:count]
    print(subject_dirs)
    print(f"Number of directories found: {len(subject_dirs)}")

    for dir_ind, directory in enumerate(subject_dirs[:2]):
        for excluded in ex_subs:
            if excluded in directory:
                print(f"Deleting {directory}")
                del subject_dirs[dir_ind]

    for subject_dir in subject_dirs:

        subject_ids.append(subject_dir.split('/')[-2])

        mat_files = glob(subject_dir + '*_Flanker/*_probeInfo.mat') + glob(subject_dir + '*_Flanker/*_probeinfo.mat')
        if len(mat_files) == 0:
            print(f"Missing probe info for {subject_dir}...\n")
            continue
        
        print(subject_dir)
        subject_dir = '/'.join(mat_files[0].split('/')[:-1])

        raw_nirx = mne.io.read_raw_nirx(subject_dir)
        raw_scans.append(raw_nirx)

        preproc_scan = preprocess(raw_nirx)
        if preproc_scan:
            preproc_scans.append(preproc_scan)

    return subject_ids, raw_scans, preproc_scans

def preprocess(scan):

    try:
        # convert to optical density
        scan.load_data() 

        raw_od = mne.preprocessing.nirs.optical_density(scan)

        # scalp coupling index
        sci = mne.preprocessing.nirs.scalp_coupling_index(raw_od)
        raw_od.info['bads'] = list(compress(raw_od.ch_names, sci < 0.5))

        if len(raw_od.info['bads']) > 0:
            print("Bad channels in subject", raw_od.info['subject_info']['his_id'], ":", raw_od.info['bads'])

        # temporal derivative distribution repair (motion attempt)
        tddr_od = mne.preprocessing.nirs.tddr(raw_od)


        bp_od = tddr_od.filter(0.01, 0.2)

        # haemoglobin conversion using Beer Lambert Law (this will change channel names from frequency to hemo or deoxy hemo labelling)
        haemo = mne.preprocessing.nirs.beer_lambert_law(bp_od, ppf=0.1)

        # bandpass filter
        haemo_bp = haemo.copy().filter(
            0.05, 0.7, h_trans_bandwidth=0.2, l_trans_bandwidth=0.02)

        return haemo_bp
    except:
        return False

def test():
    #subject_ids, raw_scans, preproc_scans = load('/storage1/fs1/perlmansusan/Active/moochie/analysis/CARE/NIRS_data_clean_2/')
    subject_ids, raw_scans, preproc_scans = load('/storage1/fs1/perlmansusan/Active/moochie/study_data/P-CAT/R56/NIRS_data/', count = 20)

    lens = hrconv.lens()

    for subject_id, raw_nirx, preproc_nirx in zip(subject_ids, raw_scans, preproc_scans):
        # Create a copy of the original scan
        convolved_nirx = preproc_nirx.copy()
        convolved_nirx.load_data()

        # Convolve the scan
        convolved_nirx = hrconv.deconvolve_hrf(convolved_nirx, filter_type = 'normal', sigma = 1, scaling_factor = 0.1, plot = True)

        lens.compare_subject(subject_id, raw_nirx, preproc_nirx, convolved_nirx, channel = 0)

    lens.compare_subjects()

def trad_glm():
    subject_ids, raw_scans, preproc_scans = load('/storage1/fs1/perlmansusan/Active/moochie/study_data/P-CAT/R56/NIRS_data/', count = 10)

    for subject_id, raw_nirx, preproc_nirx in zip(subject_ids, raw_scans, preproc_scans):
        # Grab nirs events
        
        events, event_id = mne.events_from_annotations(preproc_nirx.annotations)
        
        print(f'Events: {events}')
        print(f"Event ID's: {event_id}")

        # Define the task design
        
        design_matrix = make_first_level_design_matrix(
            preproc_nirx,
            drift_model="cosine",
            high_pass=0.005,  # Must be specified per experiment
            hrf_model="spm",
            stim_dur=5.0,
        )

        # Fit GLM
        trad_glm_results = run_glm(preproc_nirx, design_matrix)

        # Define contrast: Incongruent - Congruent
        contrast_vector = [0, 1, -1]  # Assuming the first regressor is baseline

        # Compute contrast
        trad_contrast = mne_nirs.compute_contrast(trad_glm_results, trad_glm_results, contrast_vector)

        # Visualize contrast results
        trad_contrast.plot_topo()

        # Plot and save traditional preprocessed topography of contrast
        fig = trad_contrast.plot_topo(title='Traditional Data Contrast: Incongruent - Congruent')
        fig.savefig("conv_analysis/trad_contrast_incongruent_congruent.jpeg")
        trad_contrast.save('conv_analysis/trad_contrast_results.h5')
    
def conv_glm():
    subject_ids, raw_scans, preproc_scans = load('/storage1/fs1/perlmansusan/Active/moochie/study_data/P-CAT/R56/NIRS_data/', count = 6)

    # Time resolution (TR or sampling interval, in seconds)
    time_resolution = 0.128
    regressor_headers = ['Directionality', 'Congruency', 'Direction', 'Response', 'Accuracy', 'Linear Drift', 'Intercept']

    for subject_id, raw_nirx, preproc_nirx in zip(subject_ids, raw_scans, preproc_scans):
        total_duration = preproc_nirx.n_times / preproc_nirx.info['sfreq']
        time_points = int(total_duration / time_resolution)
       
        # Populate time series based on event timings
        events, event_ids = mne.events_from_annotations(raw_nirx)

        # Initialize binary time series for each condition
        # columns - directionality, congruency, direction, response, accuracy
        design_matrix = np.zeros((time_points, 5))

        for event in events:
            for annotation, id in event_ids.items():
                if id == event[2]:
                    break
            annotation = bin(int(round(float(annotation), 0)))[3:]

            onset_index = int(event[0] / time_resolution)
            duration_index = int(1 / time_resolution)
            print(f"{onset_index} --> {onset_index + duration_index}")
            print(f"\nHRF Convolved Design Matrix:\n {design_matrix}\n\nAnnotation: {annotation}")
            design_matrix[onset_index:onset_index + duration_index, :] = annotation

        # Add a linear drift term (optional)
        #linear_drift = np.linspace(0, 1, time_points)
        #design_matrix = np.column_stack([design_matrix, linear_drift])

        # Add a constant column (intercept term)
        #intercept = np.ones(time_points)
        #design_matrix = np.column_stack([design_matrix, intercept])

        design_matrix = pd.DataFrame(design_matrix, columns = regressor_headers)
        design_matrix.to_csv("conv_analysis/conv_design_matrix.csv", index=False)

        # Create a copy of the original scan
        convolved_nirx = preproc_nirx.copy()
        convolved_nirx.load_data()

        # Convolve the scan
        convolved_nirx = hrconv.convolve_hrf(convolved_nirx)

        # Fit GLM
        conv_glm_results = run_glm(convolved_nirx, design_matrix)

        MSE = conv_glm_results.MSE()
        print(f"MSE - {MSE}")

        # Plot and save convolved topography of contrast
        fig = conv_glm_results.plot_topo()
        fig.savefig("conv_analysis/conv_contrast_incongruent_congruent.jpeg")
        contrast.save('conv_analysis/conv_contrast_results.h5')

        # Define contrast: Incongruent - Congruent
        # directionality, congruency, direction, response, accuracy, linear drift, intercept
        #    'ND' : '0', # 
        #    'D' : '1', 
        #    'I' : '0', # Congruency - .evt file column 
        #    'C' : '1',
        #    'L' : '0', # Directionality
        #    'R' : '1',
        #    'None': '0', # User response
        #    'left': '0',
        #    'right': '1',
        #    'incorrect': '0', # Accuracy
        #    'correct': '1'
        contrast_vector = [0, 1, 1, 0, 1, 0, 0]  # Assuming the first regressor is baseline

        # Compute contrast
        contrast = conv_glm_results.compute_contrast(contrast_vector)
        print(f"Contrast: {contrast}")

        print(len(convolved_nirx.info['chs']))
        print(contrast.to_dataframe())  # Should match the number of valid sensors

        # Plot and save convolved topography of contrast
        fig = contrast.plot_topo()
        fig.savefig("conv_analysis/conv_contrast_incongruent_congruent.jpeg")
        contrast.save('conv_analysis/conv_contrast_results.h5')
    

def save():
    subject_ids, raw_scans, preproc_scans = load('/storage1/fs1/perlmansusan/Active/moochie/study_data/P-CAT/R56/NIRS_data/')

    for subject_id, preproc_nirx in zip(subject_ids, preproc_scans):

        path = "/storage1/fs1/perlmansusan/Active/moochie/analysis/P-CAT/NIRS_data_clean/"
        filename = f"sub-{subject_id}_ses-0_task-flanker"

        print(f"To save {filename}")
        if os.path.exists(f"{path}preprocessed_nirs/{subject_id}") == False:
            os.mkdir(f"{path}preprocessed_nirs/{subject_id}")
            os.mkdir(f"{path}preprocessed_nirs/{subject_id}/Flanker")

        preproc_nirx.save(f"{path}preprocessed_nirs/{subject_id}/Flanker/{filename}_nirs-preprocessed.fif", overwrite=True)
        write_raw_snirf(preproc_nirx, f"{path}preprocessed_nirs/{subject_id}/Flanker/{filename}_nirs-preprocessed.snirf")

        # Create a copy of the original scan
        convolved_nirx = preproc_nirx.copy()
        convolved_nirx.load_data()

        # Convolve the scan
        convolved_nirx = hrconv.convolve_hrf(convolved_nirx)

        if os.path.exists(f"{path}convolved_nirs/{subject_id}") == False:
            os.mkdir(f"{path}convolved_nirs/{subject_id}/")
            os.mkdir(f"{path}convolved_nirs/{subject_id}/Flanker")

        convolved_nirx.save(f"{path}convolved_nirs/{subject_id}/Flanker/{filename}_nirs-convolved.fif", overwrite=True)
        
        write_raw_snirf(convolved_nirx, f"{path}convolved_nirs/{subject_id}/Flanker/{filename}_nirs-convolved.snirf")
        



if __name__ == '__main__':
    test()
