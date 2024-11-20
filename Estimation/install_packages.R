# Set a CRAN mirror
options(repos = c(CRAN = "https://cloud.r-project.org"))

# Install the required packages one by one
install.packages("DBI", dependencies = TRUE)
install.packages("rJava", dependencies = TRUE)
install.packages("DatabaseConnector", dependencies = TRUE)

# Set Java Home if installing rJava
Sys.setenv(JAVA_HOME = "/Library/Java/JavaVirtualMachines/jdk-11.0.18+10/Contents/Home") # Update this path if necessary
