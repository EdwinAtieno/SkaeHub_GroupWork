from matplotlib.backends.backend_pdf import PdfPages
import matplotlib.pyplot as plt
#converting to pdf Function
def convert_to_pdf(data,path,name):
    # fig  and ax is  for unpacking  this tuple into the variables
    # fig is useful incase you want to save as a figure later
    # ax is for objects in plotting methods
    fig, ax = plt.subplots(figsize=(12, 4))
    #resize subplots in a figure so that there are no overlaps between axes objects
    ax.axis('tight')
    #hide axes
    ax.axis('off')
    the_table = ax.table(cellText=data.values, colLabels=data.columns, loc='center')
# saves mutiples plotd to a file
    pp = PdfPages(path + name)
    #save fig
    pp.savefig(fig, bbox_inches='tight')
    # close
    pp.close()