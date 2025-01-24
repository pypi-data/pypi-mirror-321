import pytest
from typer.testing import CliRunner
from unittest.mock import Mock, patch
import pandas as pd
import altair as alt
from pathlib import Path
import sys
from io import StringIO
from duck_plot.cli import app, create_visualization, pd_to_rich_tbl

@pytest.fixture
def runner():
    return CliRunner()

@pytest.fixture
def sample_df():
    return pd.DataFrame({
        'date': ['2024-01-01', '2024-01-02', '2024-01-03'],
        'sales': [100, 150, 200],
        'quantity': [10, 15, 20]
    })

@pytest.fixture
def mock_duckdb_connection(sample_df):
    with patch('duckdb.connect') as mock_connect:
        mock_conn = Mock()
        mock_result = Mock()
        mock_result.df.return_value = sample_df
        mock_conn.execute.return_value = mock_result
        mock_connect.return_value = mock_conn
        yield mock_connect

# Test query input methods
@pytest.mark.parametrize("input_method,query", [
    ("argument", "SELECT * FROM sales"),
    ("pipe", "SELECT date, sales FROM sales"),
    ("multiline", """
        SELECT date,
               sum(sales) as total_sales
        FROM sales
        GROUP BY 1
    """)
])
def test_query_input_methods(runner, mock_duckdb_connection, input_method, query):
    if input_method == "pipe":
        result = runner.invoke(app, ["--query-only"], input=query)
    else:
        result = runner.invoke(app, [query, "--query-only"])
    assert result.exit_code == 0

# # Test chart type validation
# @pytest.mark.parametrize("chart_type,should_succeed", [
#     ("line", True),
#     ("bar", True),
#     ("pie", False),
#     ("scatter", False)
# ])
# def test_chart_type_validation(runner, mock_duckdb_connection, chart_type, should_succeed):
#     result = runner.invoke(
#         app, 
#         ["SELECT * FROM sales", "-x", "date", "-y", "sales", "-t", chart_type]
#     )
#     assert (result.exit_code == 0) == should_succeed

# Test visualization creation
@pytest.mark.parametrize("chart_type,expected_mark", [
    ("line", "line"),
    ("bar", "bar")
])
def test_create_visualization(sample_df, chart_type, expected_mark):
    chart = create_visualization(sample_df, "date", "sales", chart_type)
    assert isinstance(chart, alt.Chart)
    assert chart.mark == expected_mark
    assert chart.encoding.x.shorthand == "date"
    assert chart.encoding.y.shorthand == "sales"

# Test empty results handling
def test_empty_results_handling(runner):
    with patch('duckdb.connect') as mock_connect:
        mock_conn = Mock()
        mock_result = Mock()
        mock_result.df.return_value = pd.DataFrame()
        mock_conn.execute.return_value = mock_result
        mock_connect.return_value = mock_conn
        
        result = runner.invoke(app, ["SELECT * FROM empty", "--query-only"])
        assert result.exit_code == 1
        assert "Query returned no results" in result.stdout