import pandas as pd
import random

import sys
sys.path.insert(1, '..')
from check_data_consistency import DataConsistencyChecker

from utils import synth_test, synth_test_all_cols, kropt_test

test_id = 'UNIQUE_VALUES'
random.seed(0)

synth_patterns_cols = ['unique_vals all']
synth_exceptions_cols = ['unique_vals most']


def test_synthetic_no_nulls():
	synth_test(
		test_id,
		'none',
		synth_patterns_cols,
		synth_exceptions_cols)


def test_synthetic_one_row_nulls():
	synth_test(
		test_id,
		'one-row',
		[], # This test does not cover columns with Nulls
		[])


def test_synthetic_in_sync_nulls():
	synth_test(
		test_id,
		'in-sync',
		[],
		[])


def test_synthetic_random_nulls():
	synth_test(
		test_id,
		'random',
		[],
		[])


def test_synthetic_80_percent_nulls():
	synth_test(
		test_id,
		'80-percent',
		[],
		[])


def test_synthetic_all_cols_no_nulls():
	synth_test_all_cols(
		test_id,
		'none',
		synth_patterns_cols,
		synth_exceptions_cols)


def test_synthetic_all_cols_one_row_nulls():
	synth_test_all_cols(
		test_id,
		'one-row',
		[],
		[])


def test_synthetic_all_cols_in_sync_nulls():
	synth_test_all_cols(
		test_id,
		'in-sync',
		[],
		[])


def test_synthetic_all_cols_random_nulls():
	synth_test_all_cols(
		test_id,
		'random',
		[],
		[])


def test_synthetic_all_cols_80_percent_nulls():
	synth_test_all_cols(
		test_id,
		'80-percent',
		[],
		[])


def test_fetch_kropt():
	kropt_test(
		test_id,
		[],
		[]
	)
