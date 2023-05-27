import pandas as pd
import random

import sys
sys.path.insert(1, '..')
from check_data_consistency import DataConsistencyChecker

from utils import synth_test, synth_test_all_cols, real_test, build_default_results

test_id = 'NUMBER_ALPHA_CHARS'
random.seed(0)

synth_patterns_cols = ['number_alpha_2']
synth_exceptions_cols = ['number_alpha_3']


def test_real():
	res = build_default_results()
	res['soybean'] = (0, ['area-damaged'])
	res['abalone'] = (['Sex'], 0)
	res['SpeedDating'] = (55, 0)
	res['eucalyptus'] = (['Map_Ref', 'Latitude'], 0)
	res['credit-approval'] = (['A13'], ['A5'])
	res['splice'] = (60, 0)
	res['mushroom'] = (15, 0)
	res['profb'] = (['Overtime'], 0)
	res['anneal'] = (0, ['bc', 'exptl'])
	res['tic-tac-toe'] = (9, 0)
	res['bank-marketing'] = (['V11'], 0)
	res['kropt'] = (['white_king_col', 'white_rook_col', 'black_king_col'], 0)
	res['solar-flare'] = (['class', 'largest_spot_size', 'spot_distribution'], 0)
	real_test(test_id, res)


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
		synth_patterns_cols,
		synth_exceptions_cols)


def test_synthetic_in_sync_nulls():
	synth_test(
		test_id,
		'in-sync',
		synth_patterns_cols,
		synth_exceptions_cols)


def test_synthetic_random_nulls():
	synth_test(
		test_id,
		'random',
		synth_patterns_cols,
		synth_exceptions_cols)


def test_synthetic_80_percent_nulls():
	synth_test(
		test_id,
		'80-percent',
		synth_patterns_cols,
		synth_exceptions_cols)


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
		synth_patterns_cols,
		synth_exceptions_cols)


def test_synthetic_all_cols_in_sync_nulls():
	synth_test_all_cols(
		test_id,
		'in-sync',
		synth_patterns_cols,
		synth_exceptions_cols)


def test_synthetic_all_cols_random_nulls():
	synth_test_all_cols(
		test_id,
		'random',
		synth_patterns_cols,
		synth_exceptions_cols)


def test_synthetic_all_cols_80_percent_nulls():
	synth_test_all_cols(
		test_id,
		'80-percent',
		synth_patterns_cols,
		synth_exceptions_cols)
