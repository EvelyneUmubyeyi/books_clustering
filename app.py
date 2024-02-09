import streamlit as st
import json
from PIL import Image
import requests
from io import BytesIO

# Read the JSON file containing the product data
with open('products_js.json', 'r') as f:
    products_data = json.load(f)

# Display title
st.title('Product Clustering App')

# Group products by cluster
products_by_cluster = {}
for product in products_data:
    cluster = product['cluster']
    if cluster not in products_by_cluster:
        products_by_cluster[cluster] = []
    products_by_cluster[cluster].append(product)

# Sort the cluster numbers
sorted_clusters = sorted(products_by_cluster.keys())

# Iterate over clusters
for cluster in sorted_clusters:
    st.header(f'Cluster {cluster}')
    
    # Get products in the current cluster
    cluster_products = products_by_cluster[cluster]
    
    # Display products
    for product in cluster_products:
        # Render image
        st.image(product['image'], use_column_width=True)
            
        # Display description
        st.write(product['description'])