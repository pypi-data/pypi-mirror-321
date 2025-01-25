import re

class Tokenizer:
    def __init__(self) -> None:
        '''
        Initializing: str_to_int contains vocabulary dictionary
                      int_to_str contains inverse of vocabulary dictionary
                      text contains text to pass  
        '''
        self.str_to_int={}
        self.int_to_str={}
        self.text=""
    
    def pass_file(self,file_path,enc):
        '''
        To read text file, Need to pass 2 parameters: Path of File & Encoding  
        '''
        with open(file_path, "r", encoding=enc) as f:
            self.text=f.read()

    def fit(self) -> None:
        '''
        To create vocabulary:
        1. Preprocess text: Split according to space and special character
                            Add <|unk|> for unknown in vocabulary
                            Add <|endoftext|> when file changes
        2. Create Vocabulary with numbers: Create dictionary arranged alphabatically with key as number
        '''
        preprocessed=re.split(r'([,.:;?_!"()\']|--|\s)',self.text)
        preprocessed=[item.strip() for item in preprocessed if item.strip()]
        preprocessed.extend(["<|unk|>","<|endoftext|>"])
        all_words=sorted(set(preprocessed))
        vocab={token:integer for integer, token in enumerate(all_words)}
        self.str_to_int=vocab
        self.int_to_str={i:s for s,i in vocab.items()}

    def get_token(self) -> dict:
        '''
        Get Created tokens
        '''
        return self.str_to_int

    def get_token_decoder(self) -> dict:
        '''
        Geet inverse of encoded token
        '''
        return self.int_to_str

    def encode(self,text) -> list:
        '''
        Pass text and get encoded texts
        Same preprocessing applied at it was in fit
        Added <|unk|> in place of word if not in Vocabulary
        '''
        preprocessed=re.split(r'([,.:;?_!"()\']|--|\s)',text)
        preprocessed=[item.strip() for item in preprocessed if item.strip()]
        preprocessed=[item if item in self.str_to_int
                      else "<|unk|>" for item in preprocessed
                      ]
        ids=[self.str_to_int[s] for s in preprocessed]
        return ids
    
    def decode(self,ids) -> str:
        '''
        Decode, Encoded words and get text
        '''
        text=" ".join([self.int_to_str[i] for i in ids])
        text=re.sub(r'\s+([,.?!"()\'])', r'\1' , text)
        return text
    
# t1=TokenizerV1()
# t1.pass_file("the-verdict.txt","utf-8")
# t1.fit()
# t=t1.encode("how are you")
# print(t)
# print(t1.decode(t))