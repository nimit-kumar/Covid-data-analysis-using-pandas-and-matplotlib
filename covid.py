import pandas as pd
import matplotlib.pyplot as plt

df=pd.read_csv(r"C:\Users\nimit\Music\.vscode\project\country_wise_latest.csv")
print(df[["Confirmed"]].sum())
print(df[["Deaths"]].sum())
print(df[["Recovered"]].sum())

df["Active"]=df["Confirmed"]-df["Deaths"]-df["Recovered"]
print(df[["Active"]].sum())

# #top five
top5=df.sort_values(by="Confirmed" ,ascending=False).head(5)
print(top5[["Country/Region","Confirmed"]])

top5_death=df.sort_values(by="Deaths",ascending=False).head(5)
print(top5_death[["Country/Region","Deaths"]])

top5_recovery=df.sort_values(by="Recovered", ascending=False).head(5)
print(top5_recovery[["Country/Region","Recovered"]])
#Graphs
top5_active=df.sort_values(by="Active",ascending=False).head(5)

top5_active.plot(x="Country/Region",y="Active",kind="bar",color="orange",legend=True)
plt.xlabel("Countries")
plt.ylabel("Active Cases")
plt.title="Top 5 Countries with Highest Active Covid Cases"
plt.show()
plt.savefig("top5_active_cases.png")

region_data=df.groupby("WHO Region")["Confirmed"].sum()
region_data.plot.pie(legend=True,autopct='%1.1f%%',figsize=(8,8))
plt.title="Cases region wise"
plt.show()
plt.savefig("Region_data.png")

# #contries with zero death
zero_death=df[df["Deaths"]==0][["Country/Region","Confirmed"]]
print(zero_death)

#Recovery Rate
df["Recovery_rate"]=df["Recovered"]/df["Confirmed"]*100
recovery=df[["Country/Region","Recovery_rate"]].sort_values(by="Recovery_rate",ascending=False).head(10)
print(recovery.head())

#death rate
df['Death Rate'] = (df['Deaths'] / df['Confirmed']) * 100
death_rate=df[['Country/Region', 'Death Rate']].sort_values('Death Rate', ascending=False).head(10)
print(death_rate)

