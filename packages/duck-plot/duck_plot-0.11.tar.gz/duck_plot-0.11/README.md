# Duck Plot CLI

[![PyPI](https://img.shields.io/pypi/v/duck-plot.svg)](https://pypi.org/project/duck-plot/)
[![Changelog](https://img.shields.io/github/v/release/lvg77/duck-plot?include_prereleases&label=changelog)](https://github.com/lvg77/duck-plot/releases)
[![Tests](https://github.com/lvg77/duck-plot/actions/workflows/test.yml/badge.svg)](https://github.com/lvg77/duck-plot/actions/workflows/test.yml)
[![License](https://img.shields.io/badge/license-Apache%202.0-blue.svg)](https://github.com/lvg77/duck-plot/blob/master/LICENSE)

A command-line tool for visualizing SQL query results using DuckDB and Altair charts.

## Installation

Install this tool using `pip`:
```bash
pip install duck-plot
```
or run the cli with uvx in a temporary virtual environment:
```bash
uvx duck-plot ...
```

## Features

- Execute SQL queries against DuckDB databases or in-memory data
- Create line or bar charts from query results
- Display query results in a rich formatted table
- Support for piped input and command-line arguments
- Interactive visualizations in the browser

## Usage

### Basic Query Visualization

Create a line chart from query results:
```bash
duck-plot "SELECT date, sales FROM 'sales.csv'" -x date -y sales
```

Create a bar chart:
```bash
duck-plot "SELECT category, count(*) as total FROM 'sales.csv' GROUP BY 1" -x category -y total --type bar
```

### Using a DuckDB Database

Query an existing DuckDB database:
```bash
duck-plot "SELECT * FROM monthly_sales" -x month -y revenue --db sales.duckdb
```

### Piping Queries

Use heredoc for complex queries:
```bash
cat << EOF | duck-plot -x month -y total_sales --type bar
SELECT 
    date_trunc('month', date) as month,
    sum(sales) as total_sales 
FROM sales 
GROUP BY 1 
ORDER BY 1
EOF
```

### Query-Only Mode

You have the option to only display results without creating a chart:
```bash
duck-plot "SELECT * FROM sales LIMIT 5" --query-only
```

or use a pipe:
```bash
echo "SELECT * FROM 'sales.parquet'" | duck-plot --query-only --db sales.duckdb
```

## Options

```
Arguments:
  query                  SQL query to execute [optional if piping input]

Options:
  -x, --x TEXT          Column name for X-axis
  -y, --y TEXT          Column name for Y-axis
  -t, --type TEXT       Type of chart (line or bar) [default: line]
  -d, --db TEXT         Path to DuckDB database file [optional]
  -q, --query-only      Output query results to stdout and skip chart creation
  --help                Show this message and exit
```

## Examples

### Analyzing Time Series Data

```bash
duck-plot "
SELECT 
    date,
    moving_average(price, 7) as price_ma
FROM 'stock_prices.csv'
WHERE symbol = 'AAPL'
ORDER BY date
" -x date -y price_ma
```

### Comparing Categories

```bash
duck-plot "
SELECT 
    category,
    sum(revenue) as total_revenue
FROM 'sales.csv'
GROUP BY category
ORDER BY total_revenue DESC
LIMIT 10
" -x category -y total_revenue --type bar
```

### Interactive Data Exploration

```bash
# First view the available columns
duck-plot "FROM dataset LIMIT 1" --query-only

# Then create visualizations based on the columns
duck-plot "FROM dataset" -x timestamp -y temperature
```

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.
## Development

To contribute to this tool, first checkout the code. Then create a new virtual environment:
```bash
cd duck-plot
python -m venv venv
source venv/bin/activate
```
Now install the dependencies and test dependencies:
```bash
pip install -e '.[test]'
```
To run the tests:
```bash
python -m pytest
```
