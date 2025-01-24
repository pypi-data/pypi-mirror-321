import subprocess
import os.path

from feng_hirst_parser.utils.paths import CRFSUITE_PATH


class CRFClassifier:
    def __init__(self, name, model_type, model_path, model_file, verbose):
        self.verbose = verbose
        self.name = name
        self.type = model_type
        self.model_fname = model_file
        self.model_path = model_path

        if not os.path.exists(os.path.join(self.model_path, self.model_fname)):
            print('The model path %s for CRF classifier %s does not exist.' % (
                os.path.join(self.model_path, self.model_fname), name))
            raise OSError('Could not create classifier subprocess')

        self.classifier_cmd = '%s/crfsuite-stdin tag -pi -m %s -' % (CRFSUITE_PATH,
                                                                     os.path.join(self.model_path, self.model_fname))
        #        print self.classifier_cmd
        self.classifier = self._create_classifier()

        if self.classifier.poll():
            raise OSError(
                'Could not create classifier subprocess, with error info:\n%s' % self.classifier.stderr.readline())

        # self.cnt = 0

    def _create_classifier(self):
        classifier = subprocess.Popen(
            self.classifier_cmd,
            shell=True,
            stdin=subprocess.PIPE,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE
        )
        if classifier.poll() is not None:
            error = classifier.stderr.readline().decode('utf-8')
            raise OSError(f'Could not create classifier subprocess, with error info:\n{error}')
        return classifier

    def classify(self, vectors):
        """
        Parameters
        ----------
        vectors : list of str
            list of features, e.g. 'LEAF\tNum_EDUs=1\r'
        
        Returns
        -------
        seq_prob : float
            sequence probability
        predictions : list of (str, float) tuples
            list of predition tuples (label, probability)
        """
        self.classifier.stdin.write(('\n'.join(vectors) + "\n\n").encode())
        self.classifier.stdin.close()

        lines = [l.decode('utf-8') for l in self.classifier.stdout.readlines()]

        if self.classifier.poll():
            raise OSError('crf_classifier subprocess died')

        predictions = []
        for line in lines[1:]:
            line = line.strip()
            if line != '':
                fields = line.split(':')
                label = fields[0]
                prob = float(fields[1])
                predictions.append((label, prob))

        seq_prob = float(lines[0].split('\t')[1])

        # re-create classifier (because we had to close STDIN earlier)
        self.close_classifier()
        self.classifier = self._create_classifier()
        return seq_prob, predictions

    def close_classifier(self):
        if self.classifier:
            self.classifier.stdin.close()
            self.classifier.stdout.close()
            self.classifier.stderr.close()
            self.classifier.terminate()
            self.classifier.wait()
            self.classifier = None

    def poll(self):
        """
        Checks that the classifier processes are still alive
        """
        return self.classifier is None or self.classifier.poll() is not None

    def unload(self):
        if self.classifier and not self.poll():
            self.classifier.stdin.write(b'\n')
            self.classifier.stdin.flush()
            print(f'Successfully unloaded {self.name}')
        self.close_classifier()

    def __del__(self):
        self.close_classifier()
