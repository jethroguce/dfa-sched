
# coding: utf-8

# In[1]:


import requests


# In[2]:


HOST = 'https://www.passport.gov.ph/appointment/timeslot/available/next'


# In[34]:


def check_available(site_id):
    data = 'requestDate=2017-10-26&maxDate=2018-04-23&siteId={site_id}&slots=1'.format(site_id=site_id)
    headers = {
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'X-Requested-With': 'XMLHttpRequest',
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.62 Safari/537.36'
    }
    res = requests.post(HOST, data,  headers=headers)
    return res.json()


# In[37]:


sites = [(4, 'Aseana'), (6, 'Mega'), (8, 'Alabang')]


# In[39]:


for site in sites:
    res = check_available(site[0])
    print(site[1], res)

