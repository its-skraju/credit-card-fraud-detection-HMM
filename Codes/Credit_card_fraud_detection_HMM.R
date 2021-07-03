#Loading the Dataset
train <- read.csv("C:/Users/MSI-PC/OneDrive - IIT Kanpur/Industrial Management & Engineering/Semester 2/IME625A Introduction To Stochastic Processes And Their Applications/Stochastic Project/Data/train_data_r.csv")
test <- read.csv("C:/Users/MSI-PC/OneDrive - IIT Kanpur/Industrial Management & Engineering/Semester 2/IME625A Introduction To Stochastic Processes And Their Applications/Stochastic Project/Data/test_data_r.csv")

#Loading required libraries
library(depmixS4)
library(HMM)

#Hidden states and observational symbols
hidden_states = c(1,2,3)
symbols = c('low','medium','high')

#Initializing model
hmm_initialize = initHMM(hidden_states, symbols , c(131/143,8/143,4/143))

#Fitting the model with baumwelch algorithm
hmm_Fit = baumWelch(hmm_initialize, train$symbol)

#Testing the Model
classification <- c()
train_test<-rbind(train,test)
hmm_model<-(hmm_Fit$hmm)

#If % changes in oberving the sequence is greater than specied threshold then it is a fraud tranaction
for(i in 1:50){
  #computation of acceptance probability for training
  log_scaled_forward_probabilities = forward(hmm_model,c(as.character(train_test$symbol[i:(i+142)])))
  forward_probabilities1<-data.frame(exp(log_scaled_forward_probabilities))
  Acceptance_probability1<-sum(forward_probabilities1$X10)
  
  #computation of acceptance probability after a new transaction
  log_scaled_forward_probabilities = forward(hmm_model,c(as.character(train_test$symbol[(i+1):(i+143)])))
  forward_probabilities2 <- data.frame(exp(log_scaled_forward_probabilities))
  Acceptance_probability2<-sum(forward_probabilities2$X10)
  
  #Classification of Fraudlant transactions
  {
    if(((Acceptance_probability1-Acceptance_probability2)*100/Acceptance_probability1)>=10)
      classification <-c(classification,"Fraudlant")
    else
      classification <-c(classification,"Genuine")
  }
}
#Showing test result
test_result <- cbind(test,classification)
View(test_result)
table(test_result$classification)
