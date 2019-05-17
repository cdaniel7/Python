
# coding: utf-8

# In[13]:


import webbrowser
import time


# In[14]:


webbrowser.open('https://tinder.com/')
time.sleep(5)


# In[1]:


from pynput.keyboard import Key, Controller


# In[15]:


keyboard = Controller()


# In[16]:
while(True):
    keyboard.press(Key.right)
    time.sleep(1)
    keyboard.release(Key.right)
    