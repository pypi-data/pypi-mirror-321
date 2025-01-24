# pdcleaner

#### Description
用于清洗pandas数据表格


#### 使用示例
```python
import pandas as pd
from pdcleaner import DataSet

def test_clean_data():
    # 生成测试数据
    test_data = {
        'Column 1': [' 1,234 ', '-1,253.8', "增长369,666.0", "1,2,3", None, '-'],
        'Column 2': ['20%', '98.88%', "1，235.69%", "增长10%", '-10%', '50%'],
        'Column 3': ['  extra space  ', 'no change', "'single'", "multi\nline\rtext", '1,234.56', '25%'],
        '数据写入时间2': ['2023-10-01 12:34:56', '2023-10-02 13:45:56', '2023-10-03 14:56:57', '2023-10-04 15:07:58', '2023-10-05 16:18:59', '2023-10-06 17:29:60']
    }
    df = pd.DataFrame(test_data)

    # 调用 clean_data 函数
    cleaned_df = DataSet.clean_data(df, drop_cols=['数据写入时间2'], rename_cols={'Column 1': 'New Column 1'}, add_time=True)
    print(cleaned_df)

if __name__ == '__main__':
    test_clean_data()
```
#### Software Architecture
Software architecture description

#### Installation

1.  xxxx
2.  xxxx
3.  xxxx

#### Instructions

1.  xxxx
2.  xxxx
3.  xxxx

#### Contribution

1.  Fork the repository
2.  Create Feat_xxx branch
3.  Commit your code
4.  Create Pull Request


#### Gitee Feature

1.  You can use Readme\_XXX.md to support different languages, such as Readme\_en.md, Readme\_zh.md
2.  Gitee blog [blog.gitee.com](https://blog.gitee.com)
3.  Explore open source project [https://gitee.com/explore](https://gitee.com/explore)
4.  The most valuable open source project [GVP](https://gitee.com/gvp)
5.  The manual of Gitee [https://gitee.com/help](https://gitee.com/help)
6.  The most popular members  [https://gitee.com/gitee-stars/](https://gitee.com/gitee-stars/)
