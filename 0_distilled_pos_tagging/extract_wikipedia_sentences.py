import json
import multiprocessing
import os

import stanfordnlp

from tqdm import tqdm


def get_docs(path):
    with open(path) as f:
        for line in f:
            yield json.loads(line)['text']


def iter_doc(filenames):
    for path in filenames:
        for doc in get_docs(path):
            yield doc


class IterSentences(object):
    def __init__(self, dry=False, processes=4):
        super(IterSentences, self).__init__()
        self.dry = dry
        self.nlp = stanfordnlp.Pipeline(processors='tokenize')
        self.processes = processes

    def worker(self, doc):
        if self.dry:
            return doc
        else:
            return self.nlp(doc)

    def iter_text(self, filenames):
        pool = multiprocessing.Pool(self.processes)

        for out in pool.imap(self.worker, iter_doc(filenames)):
            yield out

        pool.terminate()


def get_filenames(path='/Users/adrozdov/Developer/wikiextractor/text'):
    for base_dir, directories, files in os.walk(path):
        for fn in files:
            yield os.path.join(base_dir, fn)


if __name__ == '__main__':

    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument('--dry', action='store_true')
    options = parser.parse_args()

    filenames = [x for x in get_filenames()]
    for nlp_doc in tqdm(IterSentences(dry=options.dry).iter_text(filenames)):
        pass
