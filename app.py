# -*- coding: utf-8 -*-
"""
Created on Sat Jul 10 10:46:49 2021

@author: Jyoti Yadav
"""

from datetime import date, timedelta
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output, State


import dash
import numpy as np
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import plotly.express as px
import plotly.graph_objects as go
import pandas as pd
from stockstats import StockDataFrame






app = dash.Dash(__name__)

server = app.server




#----------------------------------
# Layout
#----------------------------------




app.layout = html.Div([
                html.Div([
                    html.Div([
                        html.Div([
                            html.H1('JYOTI ', style = {'font-family':'Garamond, serif', 'color': '#000000'}),
                        
                        ],
                        className = 'social-icons',
                        ),
                        
                        html.Div([
                            html.Img(src = "./assets/neural.png", width = 80, height=80),
                            
                        ],
                        className = 'social-icons',
                        ),
                        
                        html.Div([
                            html.H1(' YADAV', style = {'font-family':'Garamond, serif','color': '#000000'}),
                            
                        ],
                        className = 'social-icons',
                        ),
                        
                    ],
                    className = 'main-header-line',
                    
                    ),
                    
                    
                    
                    html.Div([
                        html.P('______________________ ', style = {'color': '#000000'}),
                       
                    ],
                    className = 'dash-line',
                    ),
                        
                        
                    html.Div([
                        html.Div([
                            html.A([
                                    html.Img(
                                        src="./assets/linkedin (1).png", width = 35, height=35)
                                        
                            ], href='https://www.linkedin.com/in/jyoti-yadav-b8232969/' ),
                            
                        ],
                        className = 'social-icons'
                        ),
                        
                        html.Div([    
                            html.A([
                                    html.Img(
                                        src="./assets/github.png", width = 35, height=35)
                                        
                            ], href='https://github.com/jyotiyadav99111' ),
                            
                        ],
                        className = 'social-icons'
                        ),
                           
                           
                        html.Div([    
                            html.A([
                                    html.Img(
                                        src="./assets/medium.png", width = 35, height=35)
                                        
                            ], href='https://jyotiyadav99111.medium.com/' )
                            
                        ],
                        className = 'social-icons'
                        ),
                           
                    ],
                    className = 'social-icons-group',
                    ),
                            
                            
                    html.Div([
                        html.P('"A Data Scientist with the brains of an Economist"', style = {'color': '#000000'}),
                    ],
                    className = 'summary',
                    ),
                    
                    
                    

                ],
                className = 'app-subection',
                ),
                    
                    
                html.Div([
                    
                    
                    html.Div([
                    
                    
                        html.Div([
                        
                            html.Img(
                                            src="./assets/business.png", width = 200, height=200)
                        
                        ],
                        className = 'app-subection-one-two',
                        ),
                    
                        
                        html.Div([
                        
                            html.Div([
                                html.P("Hi, I'm Jyoti,", style = {'color': '#000000'}),
                            
                            ],
                            className = 'summary-two',
                            ),
                                
                                
                            html.Div([
                                html.P('I have 4 years of hands on experience. I am skilled for Python (pandas, scikit-learn, statsmodels, tensorflow, gensim, nltk, matplotlib, seaborn, dash, plotly, fbprophet), SQL, Hive & Pyspark. I my expertise lie in data analysis, data-visualization, dashboarding & model building (traditional & advanced machine learning models).', style = {'color': '#000000'}),
                                
                            ],
                            className = 'summary-two',
                            ),
                                

                            # html.Div([
                                
                                
                                # html.Div([    
                                        # html.A([
                                                # html.Button(
                                                    # "LinkedIn",  id='linkedin-button', n_clicks=0)
                                                    
                                        # ], href='https://www.linkedin.com/in/jyoti-yadav-b8232969/')
                                        
                                # ],
                                # className = 'button'
                                # ),   
                                
                                
                                # html.Div([    
                                        # html.A([
                                                # html.Button(
                                                    # "Github",  id='github-button', n_clicks=0)
                                                    
                                        # ], href='https://github.com/jyotiyadav99111' )
                                        
                                # ],
                                # className = 'button'
                                # ), 
                                
                                
                                # html.Div([    
                                        # html.A([
                                                # html.Button(
                                                    # "Medium",  id='medium-button', n_clicks=0)
                                                    
                                        # ], href='https://jyotiyadav99111.medium.com/')
                                        
                                # ],
                                # className = 'button'
                                # ), 
                                
                            
                            # ],
                            # className = 'button-clubed',
                            
                            # ),
                            
                            
                            html.Div([    
                                    html.Img(src="./assets/Frame 1.svg", width = 950)
                                    
                            ],
                            className = 'summary-two'
                            ),
                            
                        
                        ],
                        className = 'app-subection-one-two',
                        ),
                        
                    ],
                    className = 'photo-align',
                    ),    
                        
                        
                        
                    
                ],
                className = 'app-subection-one',
                ),
                
                
                
                html.Div([
                
                    
                    html.Div([
                                html.H1("Blogs", style = {'color': '#000000'}),
                            
                            ],
                            className = 'summary-three',
                            ),
                    
                    
                    html.Div([
                        html.P('______________________ ', style = {'color': '#000000'}),
                       
                    ],
                    className = 'dash-line',
                    ),
                    
                    
                    html.Div([    
                                        html.A([
                                                html.P('Data Science and Blockchain: A Bright future ahead' ,style = {'text-decoration': 'underline', 'font-family': 'Impact,Charcoal,sans-serif', 'font-size': '25px', 'color': '#000000'})
                                                    
                                        ], href='https://jyotiyadav99111.medium.com/data-science-and-blockchain-a-bright-future-ahead-29bfe4fb2b56'),
                                        
                       html.P("11 May'20 - 5 min read", style = {'font-family': 'ariel', 'font-size': '12px','color': '#000000'}),
                        html.P("Recently, blockchain has attracted a lot of attention from Data Scientists. There are chances that it will either become a partner just like other databases or could overtake Data Science to become the most wanted job profile. In order to understand the relationship between blockchain and data science, a basic knowledge about the block chain is required. Being a part of the data science community we already know what Data Science is and in which areas it operates...", style = {'font-family': 'Ariel', 'font-size': '18px','color': '#707B7C'}),
                       
                    
                    ],
                    className = 'blog'
                    ),  
                    
                    html.Div([
                     
                     
                    html.A([
                                                html.P('Tensorflow: Multiple Linear Regression model from scratch with calculations explained' ,style = {'text-decoration': 'underline','font-family': 'Impact,Charcoal,sans-serif', 'font-size': '25px','color': '#000000'})
                                                    
                                        ], href='https://jyotiyadav99111.medium.com/tensorflow-multiple-linear-regression-model-from-scratch-with-calculations-explained-e75d6dec820d'),
                                        
                        html.P("12 Apr'20 - 5 min read", style = {'font-family': 'ariel', 'font-size': '12px', 'color': '#000000'}),
                        html.P("For a beginner, given the pool of resources available over internet, it becomes very difficult to understand even the basics of Tensorflow. This sometimes ends up getting demotivated. Once something is left, its hard to pick it up again with the fear of losing again. So, in order to break this vicious cycle, I am writing this very easy and understandable approach for a first time learner...", style = {'font-family': 'ariel', 'font-size': '18px', 'color': '#707B7C'}),
                       
                    
                    
                    
                     
                    ],
                    className = 'blog',
                    ),
                    
                    
                    
                    html.Div([
                        
                        
                        html.A([
                                                html.P('Selecting optimal number of clusters in KMeans Algorithm(Silhouette Score)' ,style = {'text-decoration': 'underline','font-family': 'Impact,Charcoal,sans-serif', 'font-size': '25px','color': '#000000'})
                                                    
                                        ], href='https://jyotiyadav99111.medium.com/data-science-and-blockchain-a-bright-future-ahead-29bfe4fb2b56'),
                                        
                        html.P("17 Aug'19 - 3 min read", style = {'font-family': 'ariel', 'font-size': '12px', 'color': '#000000'}),
                        html.P("KMeans is a unsupervised machine learning technique primarily used for the clubbing similar instances together. In case of supervised learning, there are multiple ways of validating the results. But in case of unsupervised learning, the only way to validate the score is trough visualization. But, this technique also has its limitations which is the higher number of dimensions. While training the model, an expert is required to decide the number of the clusters that should be there. This becomes very difficult as the dimension of the data increases. There are two simple and popular methods of doing this...", style = {'font-family': 'ariel', 'font-size': '18px', 'color': '#707B7C'}),
                       
                    
                    ],
                    className = 'blog',
                    ),
                    
                    
                    html.Div([
                    
                        html.Div([    
                                            html.A([
                                                    html.Button(
                                                        "See all", style = {'font-family': 'Impact,Charcoal,sans-serif', 'font-size': '15px' }, id='read-more-button', n_clicks=0)
                                                        
                                            ], href='https://jyotiyadav99111.medium.com/')
                                            
                        ],
                        className = 'button'
                        ),   
                                
                    ],
                    className = 'blog',
                    ),
                    
                
                    
                
                ],
                className = 'app-subection-two',
                ),
                
                
                
                
                
                html.Div([
                
                
                      
                
                
                ],
                className = 'app-subection-one'
                ),
                
                
                
                
                
               
                
            
            ],
            className = 'app-main',
            )






if __name__ == "__main__":
    app.run_server(debug = True, use_reloader=False)



























