import subprocess

def main():
    subprocess.run(["pytest", "--cov=controle", "--cov-report=html"], check=True)

if __name__ == "__main__":
    main()