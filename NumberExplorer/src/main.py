import argparse
import sys

from even import generate_perfect, validate_perfect, plot_perfects
from odd import explore_odd, plot_filters


def main():
    parser = argparse.ArgumentParser(
        prog='numberexplorer',
        description='Explore even and odd perfect numbers'
    )
    subparsers = parser.add_subparsers(dest='command', required=True)

    # Even subcommand
    even_parser = subparsers.add_parser('even', help='Generate even perfect numbers')
    even_parser.add_argument(
        '--max-exponent', '-m', type=int, required=True,
        help='Maximum exponent p to test (<=31)' # Wrap help string
    )
    even_parser.add_argument(
        '--plot', action='store_true', 
        help='Show a plot of the results'
    )
    even_parser.add_argument(
        '--save', type=str, 
        help='Path to save the plot image'
    )

    # Odd subcommand
    odd_parser = subparsers.add_parser(
        'odd', help='Filter candidate odd perfect numbers'
    )
    odd_parser.add_argument(
        '--start', '-s', type=int, required=True, 
        help='Start of range'
    )
    odd_parser.add_argument(
        '--end', '-e', type=int, required=True, 
        help='End of range'
    )
    odd_parser.add_argument(
        '--workers', '-w', type=int, default=4, 
        help='Number of threads'
    )
    odd_parser.add_argument(
        '--plot', action='store_true', 
        help='Show a summary plot'
    )
    odd_parser.add_argument(
        '--save', type=str, 
        help='Path to save the plot image'
    )

    args = parser.parse_args()

    if args.command == 'even':
        p_max = args.max_exponent
        if p_max < 2 or p_max > 31:
            print('max-exponent must be between 2 and 31', file=sys.stderr)
            sys.exit(1)
        perfects = generate_perfect(p_max)
        for p, val in perfects:
            print(f'p={p} -> {val}')
        # validate
        for _, val in perfects:
            valid = validate_perfect(val)
            print(f'Valid check for {val}: {valid}')
        # Determine if plot should be shown or saved
        show_plot = args.plot
        save_plot_path = args.save
        # Only call plotting function if showing or saving
        if show_plot or save_plot_path:
            plot_perfects(perfects, show=show_plot, save_path=save_plot_path)

    elif args.command == 'odd':
        start, end = args.start, args.end
        # Wrap long condition
        if start < 1 or end < start or end > 10**6:
            print(
                'Invalid range. Ensure 1 <= start <= end <= 1e6',
                file=sys.stderr
            )
            sys.exit(1)
        results = explore_odd(start, end, workers=args.workers)
        if results:
            print('Candidates:')
            for n, reason in results:
                print(f'{n}: {reason}')
        else:
            print('No candidates found')
        # Determine if plot should be shown or saved
        show_plot = args.plot
        save_plot_path = args.save
        # Only call plotting function if showing or saving
        if show_plot or save_plot_path:
            plot_filters(results, show=show_plot, save_path=save_plot_path)


if __name__ == '__main__':
    main()
