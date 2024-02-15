# import streamlit as st
import pandas as pd
from st_aggrid import GridOptionsBuilder, AgGrid, JsCode

# Test data is copy from www.ag-grid.com
# In order to minimize the coding time, please allow me to show it in such a weird format.
data = {
    "Michael Phelps": 27,
    "Natalie Coughlin": 25,
    "Aleksey Nemov": 24,
    "Alicia Coutts": 24,
    "Missy Franklin": 17,
    "Ryan Lochte": 27,
    "Allison Schmitt": 22,
    "Natalie Coughlin": 21,
    "Ian Thorpe": 17,
    "Dara Torres": 33,
    "Cindy Klassen": 26,
}

df = pd.DataFrame({"name": data.keys(), "age": data.values()})


defaultColDef = {
    "filter": True,
    "resizable": True,
    "sortable": True,
    
}

# refer from https://www.ag-grid.com/javascript-data-grid/filter-api/#example-filter-api-readonly
# This is the keypoint. 
"""
If you have a component that you wish to work on data once it's ready
 (calculate the sum of a column for example) 
then you'll need to hook into either the gridReady 
or the firstDataRendered events.
"""
onFirstDataRendered = JsCode("""
function onFirstDataRendered(parmas) {
  var ageFilterComponent = parmas.api.getFilterInstance('age');
  ageFilterComponent.setModel({
    type: 'greaterThan',
    filter: 18,
    filterTo: null,
  });

  parmas.api.onFilterChanged();
}
""")

options = {
    "rowSelection": "multiple",
    "rowMultiSelectWithClick": True,
    # "sideBar": ["columns", 'filters'],
    "enableRangeSelection": True,
    "onFirstDataRendered": onFirstDataRendered
}

options_builder = GridOptionsBuilder.from_dataframe(df)
options_builder.configure_default_column(**defaultColDef)
options_builder.configure_grid_options(**options)
grid_options = options_builder.build()
grid_table = AgGrid(df, grid_options, allow_unsafe_jscode=True)