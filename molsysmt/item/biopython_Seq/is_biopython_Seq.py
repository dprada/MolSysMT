
def is_biopython_Seq(item):

    item_fullname = item.__class__.__module__+'.'+item.__class__.__name__
    return item_fullname == 'biopython.Seq'
