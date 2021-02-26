from astropy.io import fits
import numpy as np
import matplotlib.pyplot as plt

# Finish the new Observer class!
class Observer():
    '''
    This class creates an artificial night sky observer.
    '''
    
    # This function will get called automatically
    # when a new "observer" is created
    def __init__(self,im1_filename,im2_filename):
        '''
        When initializing the observer, the "red" image should be given
        as the first input argument and the "ir" image should be the second input
        '''
        self.im1_filename = im1_filename
        self.im2_filename = im2_filename
        self.load_images(im1_filename,im2_filename)
        
    def load_images(self, im1_filename,im2_filename):
        '''
        This function takes 2 images files names and loads them with fits
        then return a dictionary of the file name and image array for each file
        '''
        
        load_im1 = fits.getdata(im1_filename)
        load_im2 = fits.getdata(im2_filename)
        im_dict = {im1_filename: load_im1, im2_filename:load_im2}
        self.im_dict = im_dict
    
    def calc_stats(self):
        for x in self.im_dict:
            std = np.std(self.im_dict[x])
            mean = np.mean(self.im_dict[x])
            print('the standard dev is', std)
            print('the mean is', mean)

    
    def make_composite(self, f1,f2, im_dict):
        
        '''
        This function takes in the following:
        f1 : file name for the "R" filter image
        f2 : file name for the "I" filter image
        im_dict : a dictionary that contains the image arrays as entries that match the file names
        '''
        # Define the array for storing RGB values
        rgb = np.zeros((self.im1_data.shape[0],self.im1_data.shape[1],3))
        
        # Define a normalization factor for our denominator using the R filter image
        norm_factor = self.im1_data.astype("float").max()
        
        # Compute the red channel values and then clip them to ensure nothing is > 1.0
        rgb[:,:,0] = 1.5 * (self.im2_data.astype("float")/norm_factor)
        rgb[:,:,0][rgb[:,:,0] > 1.0] = 1.0
        
        rgb[:,:,1] = (im_dict[f2].astype("float")+ (im_dict[f1].astype('float')))/2 / norm_factor
        rgb[:,:,1][rgb[:,:,1] > 1.0] = 1.0
        
        rgb[:,:,2] = (im_dict[f1].astype("float")/norm_factor)
        rgb[:,:,1][rgb[:,:,1] > 1.0] = 1.0
        
        rgb[:,:,2][rgb[:,:,2] > 1.0] = 1.0
        
        return rgb