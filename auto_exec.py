import os
from datetime import datetime


def main():
    exe_path = "~/parallel/homework/makeVer/gemm_test"
    log_path = "~/parallel/homework/makeVer/log.txt"
    for c in range(100, 2001, 100):
        start = datetime.now()

        execute = f"{exe_path} {c} {c} {c} >> {log_path}"
        os.system(execute)
        end = datetime.now()
        print(f"{c} 耗时 {end - start}")


if __name__ == "__main__":
        start = datetime.now()
        print(start.strftime("%H:%M:%S"))

        main()
        end = datetime.now()
        print(f"总计耗时 {end - start}")

        
