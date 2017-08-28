'''
RIT SPEX Comms:  Twitter posting basic.

Script for automating photo posting on twitter.

Pre-Req:
    Python3
    Tweepy library twitter


Contributors:
    Evan Putnam
    Henry Yaeger
    John LeBrun
    Helen O'Connell
'''

import basicTwitter
import os


def getFiles():
    """
    Gets all image names in the current directory and returns them in a string list
    :return:
    """
    lst = []
    for file in os.listdir(os.getcwd()):
        if file.endswith(".jpg") or file.endswith(".png"):
            lst.append(file)
    print(lst)
    return lst


def getUploaded(filename):
    """
    Gets all uploaded file names from the text file.
    :param filename: Text file with uploaded image names...
    :return: lst of strings from text file that have been posted.
    """
    lst = []
    for elem in open(filename):
        t1 = elem.replace("\n", "")
        lst.append(t1)
    return lst






def updateTextFile(filename, lst):
    """
    Updates the text file with new uploaded image names
    :param filename: Name of text file used to store image names
    :param lst: List of newly added elements
    :return: NONE
    """
    with open(filename, "a") as myfile:
        for elem in lst:
            myfile.write(elem+"\n")
        myfile.close()












def checkUploadTruth(imageStr,uploadedLst):
    """
    Helper function to check if image has been uploaded in past.  Based on image names in uploadedLst
    :param imageStr: Name to check if uploaded
    :param uploadedLst: List of uploaded names
    :return: Bool True for uploaded and False for not
    """
    if imageStr in uploadedLst:
        return True
    else:
        return False

#Uploads images HELPER!!!
def uploadImages(lstDirectory,lstUploaded, api):
    """
    Upload images to Twitter from a list of images in directory against a list of ones that have already been uploaded
    :param lstDirectory: List of image names in directory
    :param lstUploaded: List of image names in text file
    :param api: API object that allows posting to twitter.
    :return: List[] of newly uploaded photos.
    """
    lst = []
    for elem in lstDirectory:
        boolTemp = checkUploadTruth(elem, lstUploaded)
        if boolTemp == True:
            print("PHOTO ALREADY POSTED:"+elem)
        else:
            #Upload and update lst
            print("POSTING FILENAME:"+elem)
            lst.append(elem)
            #Post to twitter
            basicTwitter.tweetPicture(api, elem)
    return lst


def updateTwitter(filename):
    """
    Uploads all images in working directory to twitter as long as their names do not appear in the filename.
    :param filename: File to check for image names that should not be uploaded to twitter.
    :return: NONE
    """


    #REPLACE WITH CONSUMER KEYS
    conKey = ""
    conSec = ""

    #REPLACE WITH ACCESS TOKENS
    accTok = ""
    accSec = ""

    #Get an api object
    api = basicTwitter.apiSetUp(conKey, conSec, accTok, accSec)

    #Get image file names in directory
    imageFiles = getFiles()
    #Get image file names that exist in text file
    uploadedNames = getUploaded(filename)

    #Compares images from directory from names in text file to see if they are new.
    images = uploadImages(imageFiles, uploadedNames, api)

    #Updates the text file with the newly uploaded images.
    updateTextFile(filename, images)








def automate():
    """
    Function for personal testing...
    Used to automate with python and cron.
    :return:
    """
    updateTwitter("photos.txt")




def main():
    """
    Calls the main functionality for updating twitter with all of our directory photos.
    :return:
    """
    updateTwitter(input("Enter File Name: "))

if __name__ == '__main__':
    main()





