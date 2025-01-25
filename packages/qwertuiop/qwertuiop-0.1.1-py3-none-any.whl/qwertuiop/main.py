def help():
    stringa = '''
    ################################################################################
# FORMULARIO SERIE R
################################################################################
# IMPORTO I DATI
source(file.choose())
library(forecast)
library(readxl)

s = 12

y = ts(scan(file.choose()), start=c(2008,1),frequency = s)

# STIMA DEL MODELLO
par(mfrow=c(3,1))
plot(y)
acf(y,s*8)
pacf(y,s*8)

dsy = diff(y,s)
plot(dsy)
acf(dsy,s*8)
pacf(dsy,s*8)

mod = Arima(y,order=c(1,0,1),seasonal=list(order=c(0,1,1),period=s),include.constant = F)
stat.mod(mod)

# BANDE DI CONFIDENZA
N = length(y)
soglia = 1.96/sqrt(N)
soglia
lag = 24
global = acf(mod$residuals, lag)$acf
global
partial = pacf(mod$residuals, lag)$acf
partial

for (i in 1:length(global)){
  if (abs(global[i]) > soglia){
    print(i)
  }
}

for (i in 1:length(partial)){
  if (abs(partial[i]) > soglia){
    print(i)
  }
}
#LJUNG-BOX
lbt1 = Ljung.Box.2(mod$residuals,maxlag = 24,par = 3,all = F)
lbt1

# STIMA MODELLLO CON DUMMY
md = make.dummy(N,12,1)
md

fit = lm(y~-1+md[,1]+md[,2]+md[,3]+md[,4]+md[,5]+md[,6]+md[,7]+md[,8]+md[,9]+md[,10]+md[,11]+md[,12])
summary(fit)


mean(fit$coefficients)
ideali = fit$coefficients - mean(fit$coefficients)
ideali
mean(ideali)


# STIMA DEL MODELLO CON R^2
n = length(y)
trend = c(1:n)
trend2 = trend^2
trend3 = trend^3
trend4 = trend^4

fit1 = lm(y~-1+trend)
fit2 = lm(y~-1+trend+trend2)
fit3 = lm(y~-1+trend+trend2+trend3)
fit4 = lm(y~-1+trend+trend2+trend3+trend4)
summary(fit1)
summary(fit2)
summary(fit3)
summary(fit4)

# CONFRONTO TRA MODELLI
s = 4
y = ts(read_excel(file.choose(),skip=10), start=c(1960,1),frequency = s)[,2]

plot(y)
plot(log(y))
y = log(y)

mod1 = Arima(y,order=c(2,0,0),seasonal=list(order=c(0,1,1),period=s),include.constant = T)
stat.mod(mod1)
mod1$bic
mod2 = Arima(y,order=c(1,1,1),seasonal=list(order=c(0,1,1),period=s),include.constant = T)
stat.mod(mod2)
mod2$bic

lbt1 = Ljung.Box.2(mod1$residuals,maxlag = 24,par = 3,all = F)
lbt1
lbt2 = Ljung.Box.2(mod2$residuals,maxlag = 24,par = 3,all = F)
lbt2

# RMSE
yoss = window(y,end=c(2020,4))
ynoss = window(y,start=c(2021,1))

mod1 = Arima(yoss,order=c(2,0,0),seasonal=list(order=c(0,1,1),period=s),include.constant = T)
stat.mod(mod1)
mod1$bic
mod2 = Arima(yoss,order=c(1,1,1),seasonal=list(order=c(0,1,1),period=s),include.constant = T)
stat.mod(mod2)
mod2$bic

prev1 = forecast(mod1,9)
prev2 = forecast(mod2,9)

accuracy(prev1,ynoss)
accuracy(prev2,ynoss)

# MEDIE MOBILI
s = 4
y = ts(read_excel(file.choose(),skip=10), start=c(1960,1),frequency = s)[,2]

pesi1 = rep(1/4,4)
pesi1
pesi2 = c(1,2,2,2,1)*1/8
pesi2

M1 = wma(y, order = 4, wts = pesi1, centre =TRUE, plot=F)
M2 = wma(y, order = 5, wts = pesi2, centre =TRUE, plot=F)
M1
M2

sum(pesi1^2)
sum(pesi2^2)

# 
    '''
    print(stringa)