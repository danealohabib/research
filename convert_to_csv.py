import os
import argparse
import pandas as pd


def get_all_files_paths(dir_path):
    """
    Returns paths to all files that are in given
    directory.
    """
    filesnames = list(sorted(os.listdir(dir_path)))
    filepaths = [os.path.join(dir_path, f) for f in filesnames]
    return filepaths

def parse_args():
    """
    Parses input arguments of the script and returns them.
    """
    parser = argparse.ArgumentParser()
    parser.add_argument('-i', '--input', required=True, type=str,
                        help='Path to directory with all the files.')
    parser.add_argument('-o', '--output', required=False, type=str,
                        help='Path to output directory.',
                        default='paper_titles_processed')
    args = parser.parse_args()
    return args

def convert_files_to_csv(filespaths, output_dir):
    """
    Function creates output directory if it does not already
    exists. Then loads every file from input directory
    and converts it to CSV file that is saved to output
    directory with the same name as the processed file
    had with .csv extension.
    """
    if not os.path.exists(output_dir):
        # creates output dir if does not exists
        os.makedirs(output_dir)

    for index, filepath in enumerate(filespaths, start=1):
        if index%50==0 or index==1:
            print('Processing files... {}/{}'.format(index, len(filespaths)))
        df = pd.read_csv(filepath, sep='\n', squeeze=True) # load to one column
        df = df.str.split(' ', 2, expand=True) # split each row to 3 columns by first 2 spaces
        df.columns = ['pmid', 'year', 'title'] # name the columns
        # generate output path
        filename = os.path.basename(filepath)
        outname = '{}.csv'.format(filename)
        outpath = os.path.join(output_dir, outname)
        # output as csv file
        df.to_csv(outpath, index=False, sep=',')
    print('Done!')


if __name__ == '__main__':
    args = parse_args()
    filespaths = get_all_files_paths(args.input)
    convert_files_to_csv(filespaths, args.output)
