'''
Created on 2014-02-16

@author: Wei
'''
'''
Created on 2013-02-17

@author: Vanessa Wei Feng
'''

import subprocess

from feng_hirst_parser.utils import paths


class SyntaxParser:
    
    def __init__(self):
        # -mx150m
        cmd = 'java -Xmx1000m -cp "%s/*" ParserDemo' % paths.STANFORD_PARSER_PATH

        #print("SyntaxParser cmd:", cmd)
        self.syntax_parser = subprocess.Popen(cmd, shell=True, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr = subprocess.PIPE)
    
        init = self.syntax_parser.stderr.readline()
        if not init.startswith(b'Loading parser from serialized file'):
            raise OSError('Could not create a syntax parser subprocess, error info:\n%s' % init)

    
    def parse_sentence(self, s):
        """
        Parses a sentence s
        """
        #print "%s\n" % s.strip()
        self.syntax_parser.stdin.write(b"%s\n" % s.strip())
        self.syntax_parser.stdin.flush()
        
        # Read stderr anyway to avoid problems
        cur_line = "debut"

        #need_to_fix = False
        #finished_tags = False
        finished_penn_parse = False
        finished_dep_parse = False 
        penn_parse_result = ""
        dep_parse_results = []
        #words_tags = ""

        while cur_line != "\n" or not finished_dep_parse:
            cur_line = self.syntax_parser.stdout.readline().decode('utf-8')
            
            # Check for errors
            if cur_line.strip() == "SENTENCE_SKIPPED_OR_UNPARSABLE":
                raise Exception("Syntactic parsing of the following sentence failed:" + s + "--")
            
            if cur_line.strip() == '':
                if not finished_penn_parse:
                    finished_penn_parse = True
                elif not finished_dep_parse:
                    finished_dep_parse = True 
                else:
                    break
            else:
                #if not finished_tags:
                    #words_tags = words_tags + cur_line.strip()
                if finished_penn_parse:
                    dep_parse_results.append(cur_line.strip())
                else:
                    penn_parse_result = penn_parse_result + cur_line.strip()
            '''result = result + cur_line.strip()'''
        dep_parse_result = "\n".join(dep_parse_results)
        
        return (str(penn_parse_result), '\n'.join(dep_parse_results))
    
    
    def poll(self):
        """
        Checks that the parser process is still alive
        """
        if self.syntax_parser is None:
            return True
        else:
            return self.syntax_parser.poll() != None
        
        
    def unload(self):
        if not self.syntax_parser.poll():
            print ("Successfully unloaded syntax parser")
            #self.syntax_parser.kill() # Only in Python 2.6+
            self.syntax_parser.stdin.close()
            self.syntax_parser.stdout.close()
            self.syntax_parser.stderr.close()