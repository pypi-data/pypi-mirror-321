## Usage
### Input File
The input file can be either a `.csv` or `.xlsx` file with the following structure:
| Name     | Criterion1 | Criterion2 | Criterion3 |
|----------|------------|------------|------------|
| Option1  | 250        | 16         | 12         |
| Option2  | 200        | 16         | 8          |

### Example Code
```python
from topsis.topsis import Topsis

weights = [0.25, 0.25, 0.25]
impacts = ['+', '+', '-']
result = Topsis.calculate('data.xlsx', weights, impacts)
print(result)
