#!/usr/bin/env python
# coding: utf-8

# # Reading Recipes 
# 
# Note: Data file is recipes.csv Attached with jupyter notebook
1. Start by importing NumPy as np
# In[1]:


#type your code here
import numpy as np


# 2. All of Alize’s recipes call for milk, eggs, sugar, flour, and butter. For example, her cupcake recipe calls for:
# 
# Flour Sugar Eggs Milk Butter 2 cups 0.75 cups 2 eggs 1 cups 0.5 cups Create a NumPy array that represents this data. Each element should be a number (i.e., 2 for “2 cups”). Save this array as cupcakes.

# In[15]:


#type your code here
recipes_csv = np.genfromtxt('recipes.csv', delimiter=",")
print(recipes_csv)


# In[22]:


#type your code here
recipes = np.array(recipes_csv);
cupcakes = recipes[0];
cupcakes


# 4.Display recipes using print.
# Display recipes using print.
# 
# 
# Each row represents a different recipe. Each column represents a different ingredient.
# 
# Recipe	       Cups of Flour	Cups of Sugar	Eggs	Cups of Milk	Cups of Butter
# 
# Cupcakes	         …	              …	          …	         …	              …
# 
# Pancake	             …                …	          …	         …	              …
# 
# Cookie	             …	              …	          …	         …	              …
# 
# Bread	             …	              …	          …	         …	              …

# In[23]:


#type your code here
print('Cups of flour:', recipes[0]);
print('Cups of sugar:', recipes[1]);
print('Eggs:', recipes[2]);
print('Cups of milk:', recipes[3]);
print('Cups of butter:', recipes[0]);


# 5.The 3rd column represents the number of eggs that each recipe needs.
# 
# Select all elements from the 3rd column and save them to the variable eggs.

# In[25]:


#type your code here
eggs = recipes[::,3:4];
eggs


# 6.Which recipes require exactly 1 egg? Use a logical statement to get True or False for each value of eggs.

# In[27]:


#type your code here
eggs==1


# 7.Alize is going to make 2 batches of cupcakes (1st row) and 1 batch of cookies (3rd row).
# 
# You already have a variable for cupcakes. Create a variable for cookies with the data from the 3rd row.
# 

# In[32]:


#type your code here
cookies = recipes[3]
cookies


# 8.
# Get the number of ingredients for a double batch of cupcakes by using multiplication on cupcakes. Save your new variable to double_batch.

# In[34]:


#type your code here
double_batch = 2* cupcakes;
double_batch


# 9.
# Create a new variable called grocery_list by adding cookies and double_batch.

# In[47]:


#type your code here
print('double_cupcakes:', double_batch);
print('cookies', cookies);
grocery_list = np.vstack((double_batch, cookies));
print('grocery_list', grocery_list);

