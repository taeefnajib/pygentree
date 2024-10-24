import argparse
import sys
from .tree_generator import DirectoryTreeGenerator, __version__

def main():
    parser = argparse.ArgumentParser(
        description='Generate ASCII tree representation of directory structure',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  pygentree                     # Generate tree for current directory
  pygentree /path/to/dir       # Generate tree for specific directory
  pygentree -l 2              # Limit depth to 2 levels
  pygentree -s desc           # Sort in descending order
  pygentree -d                # Show only directories
  pygentree -o tree.txt       # Save output to file
  pygentree --ignore-hidden   # Ignore hidden files and directories
        """
    )
    
    parser.add_argument('path', nargs='?', default='.',
                       help='Root directory path (default: current directory)')
    parser.add_argument('-l', '--level', type=int,
                       help='Maximum depth level to traverse')
    parser.add_argument('-s', '--sort', choices=['asc', 'desc', 'standard'],
                       default='standard',
                       help='Sort order (asc, desc, or standard)')
    parser.add_argument('-d', '--dirs-only', action='store_true',
                       help='Show only directories, ignore files')
    parser.add_argument('-o', '--output',
                       help='Output file path to save the tree')
    parser.add_argument('--ignore-hidden', action='store_true',
                       help='Ignore hidden files and directories')
    parser.add_argument('-v', '--version', action='version',
                       version=f'PyGenTree v{__version__}')

    args = parser.parse_args()

    try:
        generator = DirectoryTreeGenerator(
            args.path,
            max_level=args.level,
            sort_order=args.sort,
            dirs_only=args.dirs_only,
            ignore_hidden=args.ignore_hidden
        )
        
        if args.output:
            generator.save_tree(args.output)
            print(f"Tree saved to: {args.output}")
        else:
            print(generator.get_tree())
            
    except Exception as e:
        print(f"Error: {str(e)}", file=sys.stderr)
        sys.exit(1)

if __name__ == '__main__':
    main()