import pandas as pd
from sklearn.datasets import fetch_openml

import sys
sys.path.insert(1, '..')
from check_data_consistency import DataConsistencyChecker
from list_real_files import real_files

# Settings. Adjust these before running the tests to run a reduced set
TEST_SYNTHETIC = True
TEST_SYNTHETIC_NONES = False
TEST_SYNTHETIC_ALL_COLUMNS = False
TEST_REAL = True


def build_default_results():
	d = {dataset: ([], []) for dataset in real_files}
	return d


def real_test(test_id, expected_results_dict):
	if not TEST_REAL:
		return
	for dataset_name in real_files:
		expected_patterns_cols = expected_results_dict[dataset_name][0]
		expected_exceptions_cols = expected_results_dict[dataset_name][1]

		print(f"Testing {dataset_name}")
		fast_only = dataset_name in ['Satellite']
		try:
			data = fetch_openml(dataset_name, version=1)
		except:
			# Most datasets have a version 1, but if not, just load any version. This may result in a warning.
			data = fetch_openml(dataset_name)
		data_df = pd.DataFrame(data.data, columns=data.feature_names)

		dc = DataConsistencyChecker(verbose=-1, execute_list=[test_id])
		dc.check_data_quality(data_df, fast_only=fast_only)
		assert dc.num_exceptions == 0

		patterns_df = dc.get_patterns_summary(short_list=False)
		if type(expected_patterns_cols) == int:
			if expected_patterns_cols < 0:
				assert len(patterns_df) >= abs(expected_patterns_cols)
			else:
				assert len(patterns_df) == expected_patterns_cols
		else:
			assert ((patterns_df is None) and (len(expected_patterns_cols) == 0)) or \
					(len(patterns_df) == len(expected_patterns_cols))
			for col in expected_patterns_cols:
				assert col in patterns_df['Column(s)'].values

		exceptions_df = dc.get_exceptions_summary()
		if type(expected_exceptions_cols) == int:
			if expected_exceptions_cols < 0:
				assert len(exceptions_df) >= abs(expected_exceptions_cols)
			else:
				assert len(exceptions_df) == expected_exceptions_cols
		else:
			assert ((exceptions_df is None) and (len(expected_patterns_cols) == 0)) or \
					(len(exceptions_df) == len(expected_exceptions_cols))
			for col in expected_exceptions_cols:
				assert col in exceptions_df['Column(s)'].values


def synth_test(test_id, add_nones, expected_patterns_cols, expected_exceptions_cols, allow_more=False):
	if not TEST_SYNTHETIC:
		return
	if not TEST_SYNTHETIC_NONES and (add_nones != 'none'):
		return

	dc = DataConsistencyChecker(verbose=-1, execute_list=[test_id])
	synth_df = dc.generate_synth_data(all_cols=False, add_nones=add_nones)
	dc.check_data_quality(synth_df)

	ret = dc.get_patterns_summary(short_list=False)
	if allow_more:
		assert len(ret) >= len(expected_patterns_cols)
	else:
		assert len(ret) == len(expected_patterns_cols)
	for col in expected_patterns_cols:
		assert col in ret['Column(s)'].values

	ret = dc.get_exceptions_summary()
	if allow_more:
		assert len(ret) >= len(expected_exceptions_cols)
	else:
		assert len(ret) == len(expected_exceptions_cols)
	for col in expected_exceptions_cols:
		assert col in ret['Column(s)'].values


def synth_test_all_cols(test_id, add_nones, patterns_cols, exceptions_cols):
	if not TEST_SYNTHETIC:
		return
	if not TEST_SYNTHETIC_ALL_COLUMNS:
		return

	dc = DataConsistencyChecker(execute_list=[test_id])
	synth_df = dc.generate_synth_data(all_cols=True, add_nones=add_nones)
	dc.check_data_quality(synth_df)

	ret = dc.get_patterns_summary(short_list=False)
	for col in patterns_cols:
		assert col in ret['Column(s)'].values

	ret = dc.get_exceptions_summary()
	for col in exceptions_cols:
		assert col in ret['Column(s)'].values
