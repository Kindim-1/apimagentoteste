#!/usr/bin/env python
# coding: utf-8

# In[5]:


import nest_asyncio
import uvicorn
from api_server import app

if __name__ == "__main__":
    nest_asyncio.apply()
    uvicorn.run(app, host='0.0.0.0', port=8000)


# In[ ]:




