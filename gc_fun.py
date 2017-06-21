try:
    import gc_content
    have_gc = True
except ImportError as e:
    have_gc = False
finally:
    #dp whatever is necessary like closing files
    pass

seq = 'AGTATCGATCGTAA'

if have_gc:
    print(gc_content.gc(seq))
else:
    print (seq.count('G') + seq.count('C'))
    
