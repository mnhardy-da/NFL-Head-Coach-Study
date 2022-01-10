#!/usr/bin/env python
# coding: utf-8

# ## NFL Head Coach Hiring and Tenure Since 2000

# #### Hiring a Head Coach, firing a Head Coach, and the overall performance of a the position is one of the most discussed topics in football. The right coaching hire can make the most of a below average roster and push solid rosters into Super Bowl contention. Team Presidents, General Managers, upper level team execs, and fans are always thinking about ways to find a coach that can elevate their roster and stand the test of time. 
# 
# #### I gathered over 20 years of data on the career life cycles on head coaches, including sitting head coaches and new hires in the year 2000 to date. This reasearch project led me to the below findings and takeaways. 
# 
# * Most often people tend to overestimate how successful their next head coach will be. 
# * While college head coaches appear to be hit or miss NFL coaching prospects, they are about as successful as coaches come from within the NFL. 
# * The Rooney rule has had minimal long term effect on bringing more diversity to NFL head coaching hires.
# * NFL Head Coaches tend to improve over time.
# * NFL Head Coaches, on average, have had shorter tenures over the last 10 years. 
# 
# 
# 

# #### Below I import the necessary libraries and print "All Set!" to confirm they've been set up. Then I import the necessary spreadsheet and inspect it. 

# In[2]:


import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np



print ('All Set!')


# In[3]:


import csv


# In[117]:


coach1=pd.read_csv(r"C:\Users\Montel\Documents\6NFL_HC_FINAL_2022.csv")


# In[10]:


print(coach1)


# #### Below I use the "shape" function to confirm the size of the spreadsheet I uploaded to Python. The spreadsheet has precisely 23 columns and 170 rows of data. 

# In[6]:


coach1.shape


# In[7]:


coach1.head()


# #### Here, I use the "corr" function to determine if there are any correlations between columns in the study.  As you can see below, much of what people may think contributes to a strong coaching candidate has no correlation at all. Remember, a correlation of 1 is considered perfect positive correlation. Therefore, experience as a coordinator, position coach,  or amount of teams coached on before being hired all have no direct correlation on whether a head coach will succeed or not. 

# In[64]:


coach1.corr()


# ### Head Coach Demographics - League From

# #### In this section I explore the population of my study. We'll examine the league, race, Age, and former position of NFL head coaches over the last 20 years. 
# 
# 
# #### Lets start with the league of origin and look at the head coaching hires from the NCAA and the NFL as well as how well they did. The below data frame shows the raw totals of hires from each league since 2000, as one can see, the NFL has been very conservative hiring college head coaches to becoming NFL head coaches to this point. 

# In[12]:


LEVEL_2 = coach1.groupby('League From').size()
print(LEVEL_2)


# #### To evaluate look at the performace of each origin of head coach, I aggregated the cumulative win percentages of each. The finding in the below dataframe and line graph were very intriguing. The head coaching hires from the NCAA had a win percentage of just one percent lower and just two percent lower in the playoffs.

# In[22]:


level = coach1.groupby(['League From'])['win percentage '].aggregate('mean')
print(level)


# In[73]:


level = coach1.groupby(['League From'])['playoff win percentage'].aggregate('mean')
print(level)


# In[23]:


sns.relplot(x="win percentage ", y="Seasons", hue="League From",
             height=4,
            kind="line", estimator=None, data=coach1);


# #### As you can see in the above line chart, the hires from college kept up with the success of NFL hires very well. One takeaway regarding why the NFL may shy away from college coaches could be becuase the small sample size small and the potential overestimation the success head coaches that were already working in the NFL when they were hired.
# 
# #### With the exception of Bill Belichick, who, on his own, makes up that large spike at the end over the chart abve the 20 season level. To visualize his sucess when compared against the typical head coach in this span, could be a research project in itself. 

# ### Head Coach Demographics - Race

# #### In 2003, the NFL adopted the Rooney rule. This rule, named after Dan Rooney, the former owner of the Pittsburgh Steelers, requires league teams to interview eminority candidates for head coaching and senior football operation jobs (https://bit.ly/32VGnnu).
# 
# #### This rule came about after former players and high profile lawyers of color conducted a study in the wake of both Dennis Green and Tony Dungy's firings. They determined that despite being, on average, more successful than their white counterparts, african american and other minorites were hired and fired at disproportionate levels (https://www.newyorker.com/sports/sporting-scene/what-work-remains-for-the-rooney-rule). Therefore, I found it important to evaluate the NFL on this effort over the last 20 years with this in mind. 

# In[26]:


diverse_3 = coach1.groupby(['RACE'])['HC'].aggregate('count')
print(diverse_3)


# #### The above dataframe shows there have been 28 minority head coaches hired since 2000, and 24, since the Rooney Rule was was adopted. This total does include names that were hired multiple times (ex: Lovie Smith, Dennis Green, and Ron Rivera are counted twice on this list.
# 
# #### You can see in the visualization and data frame below, how the winning percentage stack up and have changed over the years. Minority candidates are within a four percent margin of white candaidates, despite the large hiring disparity.

# In[61]:


diverse = coach1.groupby(['RACE'])['win percentage '].aggregate('mean')
print(diverse)


# In[55]:


sns.relplot(x="Year ", y="win percentage ", hue="RACE", kind="line",
            col="RACE", data=coach1);


# ### Head Coach Demographics - Age

# #### I decided to take a brief look at age and it appears there's no correlation between coaching age and performance. Therefore, theres not much of a reason to suggest certain candidates are "too old" or " too young" to become an at least average head coach

# In[65]:


coach1.groupby(['Age'])['win percentage '].aggregate('mean')


# ### NFL HIRING TENDENCIES AND FREQUENCY

# #### The NFL hires head coaches frequently. I'll explore just how frequently for each team hires a new coach, what the average NFL head coach tenure is, the average win percentage of a head coach, and how coaching performance changes over time. 
# 
# #### Below are the the teams with the most head coaches hired over the last 21 years sorted in descending order. The Browns, Raiders, Lions, and the Bills have the highest amount of coaching hires in that span.

# In[70]:


firing_squad = coach1.groupby(['New Team'])['HC'].aggregate('count').sort_values(ascending=False)
print(firing_squad)


# #### Below is the count of openings per year, the years prior to 2000 are just me adding the sitting head coaches for their respective teams. The year 2000 and later years have precise counts on NFL coach openings per season.

# In[66]:


firing_squad = coach1.groupby(['Year '])['New Team'].aggregate('count')
print(firing_squad)


# ### NFL Head Coach Performance Over Time

# #### From the previous section, one can gather that some NFL executives aren't afraid to fire quickly until they know they have found a coach that is a winner. Lets take a look at the below data to see: average tenure, average win percentage, and how coaches tend to perform after their first NFL head coaching job to see how justified these quick decisions are.
# 
# #### Below, I calculated the average tenure which comes out to nearly 4.5 seasons and win percentage which comes out to 44%. 
# 

# In[74]:


coach1["Seasons"].mean()


# In[77]:


coach1['win percentage '].mean()


# #### Just as in the previous section, the coaches prior to 2000 are the product of me adding in sitting coaches so don't worry about charts fpr those years. Also, don't worry about the coaches from 2017 on as most of those coaches are still sitting in their roles. I shared this to show that average tenure may shrink soon if this pattern continues.

# In[78]:


g = sns.FacetGrid(coach1, col= "Year ", col_wrap= 5,height=3,)
g.map(sns.histplot, "Seasons")


# #### Below is a look at the win percentage of head coaches in their first, second, third and fourth head coaching role. On average, head coaches have done about the same from their first to second job, but significantly better in their third and fourth role.

# In[72]:


hire =coach1.groupby(['HC JOB'])['win percentage '].aggregate('mean')
print(hire)


# #### This finding interested me, so I wanted to explore the relationship between seasons coached and win percentage from this study. Take a look at the line chart below.

# In[84]:


df = pd.DataFrame(dict(time=np.arange(500),
                       value=np.random.randn(500).cumsum()))
g = sns.relplot(x="win percentage ", y="Seasons", kind="line", data=coach1)


# #### Theres two schools of thought on this chart (maybe more): One is "of course winning coaches coach more seasons", Another is "perhaps a coach, when given enough time, can become a winner". Lets remember, the average win percentage is 44.6%, therefore someone that can win a little more than that may be more successful than their potential replacement. 
# 
# #### The below charts visualize this point, the below confirms that people tend to overestimate the success of their next head coach compared to their current one. Narratives aside, it may surprise you how well a coach is doing compared to a teams recent history hiring at the position. I compare win percentages over time for each team to pose the question: "Was the new head coach really better than the fired one?".  Also, for coaches that will be fired in January 2022: "How well are they doing compared to past hires?"

# In[112]:


g = sns.FacetGrid(coach1, col="New Team", col_wrap=4, height=2, ylim=(0, 90))
g.map(sns.pointplot, "Year ", "win percentage ", ci=None)


# #### Lastly, the below chart shows coaching performances for each coaching class (head coaches hired the same year) and how each year's class developed over time. Keep in mind some of these guys were fired, as you can see above. 

# In[113]:


sns.relplot(x="Seasons", y="win percentage ", hue="Year ",
            col="Year ", height=3, col_wrap=5,
            kind="line", estimator=None, data=coach1);


# ### Conclusion
# 
# #### Just as I mentioned in the beginning, each of my insights were proven true in this study. 
# * Most often people tend to overestimate how successful their next head coach will be. 
# * While college head coaches appear to be hit or miss NFL coaching prospects, they are about as successful as coaches come from within the NFL. 
# * The Rooney rule has had minimal long term effect on bringing more diversity to NFL head coaching hires.
# * NFL Head Coaches tend to improve over time.
# * NFL Head Coaches, on average, have had shorter tenures over the last 10 years. 
# 
# #### I think the most sobering thing about this study is that people largely overestimate what an average win percentage and record is for a NFL head coach. Given that average is just shy of a 45% win percentage, your average record is really 7-9, not the 8-8 many would assume given the 16 game regular season. Therefore with the schedule expanding to 17 games, your average record would be about 7-10. The optics on that aren't very good, but thats the reality and this record may be perceived as worse than it is. This leaves me with a few discussion questions for readers:
# 
# #### Through my data I haven't noticed a pattern that is more correlative to successful head coaches than seasons coached. Given how many coaches improve over time, how many records similiar to 7-10 will head coaches be allowed to amass before they are fired? Will this cause more churn (hiring and firing of head coaches)?
# 
# #### Not to be lost in this finiding is the fact that NCAA head coaches have held their own in the NFL when compared to their peers through data. Now that it is proven that NFL coaches aren't as successful as many think, will we see more college coaches in the NFL?
# 
# #### Lastly, minority candidates are vastly underrepresented in the NFL. The Rooney Rules' effect seems to be minimal at this point, what will it take for the NFL to make a stronger effort to promote and hire more people of color? 

# ### Future Research
# 
# #### * It may be worth looking into Bill Belichick's career, of course we know he's in the "greatest ever" conversation but his dominance over coaches in his era is worth investigating further. 
# 
# #### The validity of coaching trees. In many cases, I've find many head coaches coached under mutiple guys for many years, assigning a coach to a certain tree is tough to do solely based on resume. 

# 
