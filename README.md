# lgs-email-report

For DEV,STG run
1. Change the docker variable RUN_ENV to development or stage
2. Build docker image by running command **./dbuild-dev.sh && ./drun-dev.sh**
3. To push leads records to output topic run command **python main.py current_data(YYYY-MM-DD)**
