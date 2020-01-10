predictions:


# Imports from 3rd party libraries
import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import dash_daq as daq
from joblib import load

# Imports from this application
from app import app
# loAd pipeline

pipeline = load('assets/pipeline.joblib')
print('Pipeline Loaded!')

# 2 column layout. 1st column width = 4/12
# https://dash-bootstrap-components.opensource.faculty.ai/l/components/layout
column1 = dbc.Col(
    [
        dcc.Markdown(
            """
        
            #### Set the parametres to your preference.

            Select Wind Direction.

            """
        ),
        dcc.Slider(
        id='slider1',    
        min=0,
        max=360,
        step=45,
        value=0,
        marks={0: 'North',
               45: 'NE',
               90: 'East',
               135: 'SE',
               180: 'South',
               225: 'SW',
               270: 'West',
               315: 'NW',
               360: 'North'},
        className='mb-5'
        ),

        dcc.Markdown(
            """
        
            

            Select Swell direction.

            """
        
), 

        dcc.Slider(
        id='slider2',    
        min=0,
        max=360,
        step=45,
        value=0,
        marks={0: 'North',
               45: 'NE',
               90: 'East',
               135: 'SE',
               180: 'South',
               225: 'SW',
               270: 'West',
               315: 'NW',
               360: 'North'},
        className='mb-5'       
         ), 

         dcc.Markdown(
            """
        
            

            Select Wind Speed.

            """
        
), 
        dcc.Slider(
        id='slider3',    
        min=0,
        max=40,
        step=2,
        value=0,
        marks={0: 'No wind',
               10: 'Moderate wind',
               20: 'Windy',
               30: 'Storm',
               40: 'Hurricane',},
        className='mb-5'       
         ), 

         dcc.Markdown(
            """
        
            

            Select the month.

            """
        
), 

        dcc.Slider(
        id='slider4',    
        min=1,
        max=12,
        step=1,
        value=0,
        marks={9: 'Sep',
               1: 'Jan',
               2: 'Feb',
               3: 'Mar',
               4: 'Apr',
               5: 'May',
               6: 'June',
               7: 'Jul',
               8: 'Aug',
               10: 'Oct',
               11: 'Nov',
               12: 'Dec'},
        className='mb-5'       
         ), 

          dcc.Markdown(
            """
        
            

            Select the Wave Height.

            """
        
), 

        dcc.Slider(
        id='slider5',    
        min=0,
        max=20,
        step=2,
        value=0,
        marks={1: 'Flat',
               3: 'Small',
               6: 'Midzise',
               9: 'Perfect',
               12: 'Tubing',
               15: 'Big',
               18: 'Huge',
               20: 'Be Safe',
               },
        className='mb-5'       
         ), 


         dcc.Markdown(
            """
        
            

            Select the Dominant Swell Period.

            """
        
), 

        dcc.Slider(
        id='slider6',    
        min=1,
        max=20,
        step=1,
        value=0,
        marks={1: '1 sec',
               4: '4 sec',
               8: '8 sec',
               12: '12 sec',
               16: '16 sec',
               20: '20 sec',
               },
        className='mb-5'       
         ),

         dcc.Markdown(
            """
        
            

            Select Average Wave Period.

            """
        
), 

        dcc.Slider(
        id='slider7',    
        min=1,
        max=20,
        step=2,
        value=0,
        marks={1: '1 sec',
               4: '4 sec',
               8: '8 sec',
               12: '12 sec',
               16: '16 sec',
               20: '20 sec',
               },
        className='mb-5'       
         ),  
                      
    ],
    md=4,
)

column2 = dbc.Col(
    [
        daq.Gauge(
        id='daq1',    
        color={"gradient":True,"ranges":{"blue":[10,15],"green":[15,19],"red":[19,28]}},
        showCurrentValue=True,
        units="Degrees Celsius",
        value=0,
        label='Predicted Water Temperature' ,
        max=28,
        min=10,
        ),
        # daq.Gauge(
        # id='daq2',    
        # color={"gradient":True,"ranges":{"blue":[0,100],"orange":[100,220],"green":[220,360]}},
        # showCurrentValue=True,
        # units="Degrees, with 0 being true North",
        # value=260,
        # label='Swell Direction',
        # max=360,
        # min=0,
        # ),
        # daq.Gauge(
        # id='daq3',    
        # color={"gradient":True,"ranges":{"green":[0,10],"yellow":[10,20],"pink":[20,30],"red":[30,40]}},
        # showCurrentValue=True,
        # units="Degrees, with 0 being true North",
        # value=18.1,
        # label='Wind Speed',
        # max=40,
        # min=0,
        # ) 
        
    ]
)

layout = dbc.Row([column1, column2])


# @app.callback(
#     Output(component_id='daq1', component_property='value'),
#     [Input(component_id='slider1', component_property='value')]
# )
# def update_output_div(input_value):
#     return (input_value)


# @app.callback(
#     Output(component_id='daq2', component_property='value'),
#     [Input(component_id='slider2', component_property='value')]
# )
# def update_output_div(input_value):
#     return (input_value)


@app.callback(
    Output(component_id='daq1', component_property='value'),
    [Input(component_id='slider3', component_property='value')]
)
def update_output_div(input_value):
    return (input_value)
