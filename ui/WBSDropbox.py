#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
This is where the code will live that allows WBSTools to talk to Dropbox
'''
# Include the Dropbox SDK
import dropbox

# Get your app key and secret from the Dropbox developer website
app_key = 'llb32ihfx5t3v47'
app_secret = 'mq5hgclgqidv5mn'

flow = dropbox.client.DropboxOAuth2FlowNoRedirect(app_key, app_secret)

'''authorize_url = flow.start()
print '1. Go to: ' + authorize_url
print '2. Click "Allow" (you might have to log in first)'
print '3. Copy the authorization code.'

code = raw_input("Enter the authorization code here: ").strip()

# This will fail if the user enters an invalid authorization code'''
'''access_token, user_id = flow.finish(code)
print access_token'''
access_token = 'X4pne0V74-EAAAAAAAAAAZ3MFR-XVNQv9I1J8YLUnQfGA1X1CjY0qa0IkMAaQCwe'
client = dropbox.client.DropboxClient(access_token)
print 'linked account: ', client.account_info()
folder_metadata = client.metadata('/')
print "metadata:", folder_metadata