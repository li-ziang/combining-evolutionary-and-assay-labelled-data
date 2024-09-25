import pandas as pd
import subprocess

# 读取 CSV 文件
df = pd.read_csv('/work/commons/proteingym/DMS_substitutions.csv')

# 过滤 coarse_selection_type 列中的指定值
filtered_df = df[df['coarse_selection_type'].isin(['Binding', 'Activity', 'Expression','OrganismalFitness'])]
# print(len(filtered_df))
# 遍历每一行并执行相应的命令
for i, row in filtered_df.iterrows():

    cmd = f"python src/evaluate.py {row.DMS_id} core --n_seeds=20 --n_threads=20 --n_train=240"
#    python src/evaluate.py CCDB_ECOLI_Adkar_2012 core --n_seeds=1 --n_threads=1 --n_train=240
    
    # 打印要执行的命令（可选，用于调试）
    print(f"Running: {cmd}")
    
    # 使用 subprocess 来运行命令
    subprocess.run(cmd, shell=True)
    
    
