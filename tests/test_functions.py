import unittest
import sys
import functions
import artist


class TestFunctions(unittest.TestCase):

    def test_createObjectList(self):
        actual = functions.createObjectList([{'name_surname': 'Claude Monet', 
                                                'birthday': '14/11/1840', 
                                                'gender': 'Male', 
                                                'nationality': 'French',
                                                'ydeath': '1926', 
                                                'movement': 'Impressionism'
        }])
        oggetto = artist.Artist('Claude Monet','14/11/1840','Male','French','1926','Impressionism')
        lista=[]
        lista.append(oggetto)
        assert lista[0].name_surname == actual[0].name_surname
        
    def test_search(self):
        actual = functions.search('Caravaggio')
        oggetto = artist.Artist('Caravaggio','29/9/1571','Male','Italian','1610','Baroque')
        lista=[]
        lista.append(oggetto)
        assert lista[0].name_surname == actual[0].name_surname

if __name__ == '__main__':
    unittest.main()
