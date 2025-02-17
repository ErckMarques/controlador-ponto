from controle.cli import create_parser

def main():
    parser = create_parser()
    args = parser.parse_args()

if __name__ == '__main__':
    main()