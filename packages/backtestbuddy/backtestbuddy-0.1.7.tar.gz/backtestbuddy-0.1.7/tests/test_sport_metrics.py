import pytest
import pandas as pd
import numpy as np
from backtestbuddy.metrics.sport_metrics import *

@pytest.fixture
def sample_data():
    return pd.DataFrame({
        'bt_date_column': pd.date_range(start='2023-01-01', periods=11),
        'bt_starting_bankroll': [1000] * 11,
        'bt_ending_bankroll': [1000, 1100, 1050, 1200, 1150, 1300, 1250, 1400, 1350, 1500, 1500],
        'bt_profit': [0, 100, -50, 150, -50, 150, -50, 150, -50, 150, 0],
        'bt_win': [False, True, False, True, False, True, False, True, False, True, None],
        'bt_odds': [1.5, 2.0, 1.8, 2.2, 1.9, 2.1, 1.7, 2.3, 1.6, 2.4, None],
        'bt_stake': [100] * 10 + [0],
        'bt_bet_on': [0, 1, 0, 1, 0, 1, 0, 1, 0, 1, -1]  # Added this line
    })

class TestCalculateROI:
    def test_calculate_roi(self, sample_data):
        assert calculate_roi(sample_data) == pytest.approx(0.5)

    def test_calculate_roi_no_change(self):
        data = pd.DataFrame({'bt_starting_bankroll': [1000], 'bt_ending_bankroll': [1000]})
        assert calculate_roi(data) == 0

class TestCalculateSharpeRatio:
    def test_calculate_sharpe_ratio(self, sample_data):
        assert calculate_sharpe_ratio(sample_data) > 0

class TestCalculateMaxDrawdown:
    def test_calculate_max_drawdown(self, sample_data):
        assert calculate_max_drawdown(sample_data) == pytest.approx(-0.0454545, rel=1e-5)

class TestCalculateWinRate:
    def test_calculate_win_rate(self, sample_data):
        assert calculate_win_rate(sample_data) == 0.5

    def test_calculate_win_rate_empty_dataframe(self):
        data = pd.DataFrame({
            'bt_stake': [],
            'bt_bet_on': [],
            'bt_win': []
        })
        assert calculate_win_rate(data) == 0

    def test_calculate_win_rate_no_bets(self):
        data = pd.DataFrame({
            'bt_stake': [0, 0, 0],
            'bt_bet_on': [-1, -1, -1],
            'bt_win': [None, None, None]
        })
        assert calculate_win_rate(data) == 0

    def test_calculate_win_rate_all_wins(self):
        data = pd.DataFrame({
            'bt_stake': [100, 100, 100],
            'bt_bet_on': [0, 1, 0],
            'bt_win': [True, True, True]
        })
        assert calculate_win_rate(data) == 1.0

    def test_calculate_win_rate_mixed(self):
        data = pd.DataFrame({
            'bt_stake': [100, 0, 100, 100, 0],
            'bt_bet_on': [0, -1, 1, 0, -1],
            'bt_win': [True, None, False, True, None]
        })
        assert calculate_win_rate(data) == 2/3

class TestCalculateAverageOdds:
    def test_calculate_average_odds(self, sample_data):
        assert calculate_average_odds(sample_data) == pytest.approx(1.95)

    def test_calculate_average_odds_empty(self):
        data = pd.DataFrame({'bt_odds': []})
        assert np.isnan(calculate_average_odds(data))

class TestCalculateTotalProfit:
    def test_calculate_total_profit(self, sample_data):
        assert calculate_total_profit(sample_data) == 500

class TestCalculateAverageStake:
    def test_calculate_average_stake(self, sample_data):
        assert calculate_average_stake(sample_data) == 100

    def test_calculate_average_stake_with_zero_stakes(self):
        data = pd.DataFrame({
            'bt_stake': [100, 100, 0, 100, 0]
        })
        assert calculate_average_stake(data) == 100

    def test_calculate_average_stake_all_zero(self):
        data = pd.DataFrame({
            'bt_stake': [0, 0, 0]
        })
        assert calculate_average_stake(data) == 0

class TestCalculateSortinoRatio:
    def test_calculate_sortino_ratio(self, sample_data):
        assert calculate_sortino_ratio(sample_data) > 0

class TestCalculateCalmarRatio:
    def test_calculate_calmar_ratio(self, sample_data):
        assert calculate_calmar_ratio(sample_data) > 0

class TestCalculateDrawdowns:
    def test_calculate_drawdowns(self, sample_data):
        max_dd, max_dur = calculate_drawdowns(sample_data)
        assert max_dd == pytest.approx(0.0454545, rel=1e-5)
        assert max_dur == 2

    def test_calculate_drawdowns_no_drawdown(self):
        data = pd.DataFrame({'bt_ending_bankroll': [1000, 1100, 1200, 1300]})
        max_dd, max_dur = calculate_drawdowns(data)
        assert max_dd == 0.0
        assert max_dur == 0

    def test_calculate_drawdowns_empty_data(self):
        data = pd.DataFrame({'bt_ending_bankroll': []})
        max_dd, max_dur = calculate_drawdowns(data)
        assert max_dd == 0.0
        assert max_dur == 0

class TestCalculateBestWorstBets:
    def test_calculate_best_worst_bets(self, sample_data):
        best, worst = calculate_best_worst_bets(sample_data)
        assert best == 150
        assert worst == -50

class TestCalculateHighestOdds:
    def test_calculate_highest_odds(self, sample_data):
        highest_win, highest_lose = calculate_highest_odds(sample_data)
        assert highest_win == 2.4
        assert highest_lose == 1.9

class TestCalculateAllMetrics:
    def test_calculate_all_metrics(self, sample_data):
        metrics = calculate_all_metrics(sample_data)
        assert isinstance(metrics, dict)
        assert len(metrics) > 0
        assert metrics['ROI [%]'] == pytest.approx(50.0)
        assert metrics['Total Profit [$]'] == 500
        assert metrics['Win Rate [%]'] == 50.0
        assert metrics['Total Bets'] == 10

class TestCalculateAverageROIPerBet:
    def test_consistent_profits(self):
        """Test case with consistent profits"""
        data = pd.DataFrame({
            'bt_stake': [100, 100, 100],
            'bt_profit': [20, 20, 20],
            'bt_bet_on': [1, 1, 1]
        })
        assert calculate_avg_roi_per_bet(data) == 20.0  # (20/100) * 100 = 20%

    def test_mixed_profits_losses(self):
        """Test case with mixed profits and losses"""
        data = pd.DataFrame({
            'bt_stake': [100, 100, 100],
            'bt_profit': [50, -50, 0],
            'bt_bet_on': [1, 1, 1]
        })
        assert calculate_avg_roi_per_bet(data) == 0.0  # Average of (50%, -50%, 0%) = 0%

    def test_empty_dataframe(self):
        """Test case with empty DataFrame"""
        data = pd.DataFrame({
            'bt_stake': [],
            'bt_profit': [],
            'bt_bet_on': []
        })
        assert calculate_avg_roi_per_bet(data) == 0.0

    def test_no_bets_placed(self):
        """Test case with no bets placed"""
        data = pd.DataFrame({
            'bt_stake': [0, 0, 0],
            'bt_profit': [0, 0, 0],
            'bt_bet_on': [-1, -1, -1]
        })
        assert calculate_avg_roi_per_bet(data) == 0.0

class TestCalculateAverageROIPerYear:
    def test_single_year_profits(self):
        """Test case with single year consistent profits"""
        data = pd.DataFrame({
            'bt_date_column': pd.to_datetime(['2023-01-01', '2023-06-01', '2023-12-31']),
            'bt_starting_bankroll': [1000] * 3,
            'bt_ending_bankroll': [1000, 1200, 1500],
            'bt_profit': [0, 200, 300],
            'bt_bet_on': [1, 1, 1]
        })
        # Total ROI = (1500 - 1000) / 1000 = 0.5 = 50%
        # Time period = 1 year
        # Annual ROI ≈ 50%
        assert calculate_avg_roi_per_year(data) == pytest.approx(50.0, rel=5e-2)

    def test_multiple_years_mixed(self):
        """Test case with multiple years and different performance"""
        data = pd.DataFrame({
            'bt_date_column': pd.to_datetime([
                '2021-01-01',  # Start
                '2023-12-31'   # End (3 years)
            ]),
            'bt_starting_bankroll': [1000] * 2,
            'bt_ending_bankroll': [1000, 2500],
            'bt_bet_on': [1, 1]
        })
        # Total ROI = (2500 - 1000) / 1000 = 1.5 = 150%
        # Time period = 3 years
        # Annual ROI ≈ 50%
        assert calculate_avg_roi_per_year(data) == pytest.approx(50.0, rel=5e-2)

    def test_partial_year(self):
        """Test case with partial year"""
        data = pd.DataFrame({
            'bt_date_column': pd.to_datetime([
                '2023-01-01',  # Start
                '2023-06-30'   # End (0.5 years)
            ]),
            'bt_starting_bankroll': [1000] * 2,
            'bt_ending_bankroll': [1000, 1250],
            'bt_bet_on': [1, 1]
        })
        # Total ROI = (1250 - 1000) / 1000 = 0.25 = 25%
        # Time period ≈ 0.5 years (180 days)
        # Annual ROI ≈ 50%
        assert calculate_avg_roi_per_year(data) == pytest.approx(50.0, rel=5e-2)

    def test_empty_dataframe(self):
        """Test case with empty DataFrame"""
        data = pd.DataFrame({
            'bt_date_column': pd.Series(dtype='datetime64[ns]'),
            'bt_starting_bankroll': [],
            'bt_ending_bankroll': [],
            'bt_bet_on': []
        })
        assert calculate_avg_roi_per_year(data) == 0.0  # Keep exact comparison for edge case

    def test_same_day(self):
        """Test case with same day (zero years)"""
        data = pd.DataFrame({
            'bt_date_column': pd.to_datetime(['2023-01-01', '2023-01-01']),
            'bt_starting_bankroll': [1000, 1000],
            'bt_ending_bankroll': [1000, 1100],
            'bt_bet_on': [1, 1]
        })
        assert calculate_avg_roi_per_year(data) == 0.0  # Keep exact comparison for edge case

class TestCalculateRiskAdjustedAnnualROI:
    def test_normal_case_multi_year(self):
        """Test case with multiple years, positive returns and drawdown"""
        data = pd.DataFrame({
            'bt_date_column': pd.to_datetime([
                '2021-01-01',  # Start
                '2023-12-31'   # End (3 years)
            ]),
            'bt_starting_bankroll': [1000] * 2,
            'bt_ending_bankroll': [1000, 1150],  # 15% total ROI over 3 years ≈ 5% annual
            'bt_bet_on': [1] * 2
        })
        # Total ROI = (1150 - 1000) / 1000 = 0.15 = 15%
        # Time period = 3 years
        # Annual ROI ≈ 5%
        # Max drawdown = 0
        # Risk-adjusted = 0 (due to no drawdown)
        result = calculate_risk_adjusted_annual_roi(data)
        assert result == pytest.approx(5.0, rel=5e-2)

    def test_complete_loss_multi_year(self):
        """Test case with complete loss over multiple years"""
        data = pd.DataFrame({
            'bt_date_column': pd.to_datetime([
                '2021-01-01',  # Start
                '2023-12-31'   # End (3 years)
            ]),
            'bt_starting_bankroll': [1000] * 2,
            'bt_ending_bankroll': [1000, 800],  # -20% total ROI over 3 years ≈ -6.67% annual
            'bt_bet_on': [1] * 2
        })
        # Total ROI = (800 - 1000) / 1000 = -0.2 = -20%
        # Time period = 3 years
        # Annual ROI ≈ -6.67%
        # Max drawdown = 0.2
        # Risk-adjusted ≈ -33.35
        result = calculate_risk_adjusted_annual_roi(data)
        assert result < 0
        assert result == pytest.approx(-33.35, rel=5e-2)

    def test_no_drawdown_multi_year(self):
        """Test case with no drawdown over multiple years"""
        data = pd.DataFrame({
            'bt_date_column': pd.to_datetime([
                '2021-01-01',  # Start
                '2023-12-31'   # End (3 years)
            ]),
            'bt_starting_bankroll': [1000] * 2,
            'bt_ending_bankroll': [1000, 1300],  # 30% total ROI over 3 years ≈ 10% annual
            'bt_bet_on': [1] * 2
        })
        # Total ROI = (1300 - 1000) / 1000 = 0.3 = 30%
        # Time period = 3 years
        # Annual ROI ≈ 10%
        # Max drawdown = 0
        # Risk-adjusted = 0 (due to no drawdown)
        assert calculate_risk_adjusted_annual_roi(data) == pytest.approx(10.0, rel=5e-2)