year = 2020


if(year %% 4 == 0 && year %% 100 != 0 || year %% 4 == 0 && year %% 100 == 0  && year %% 400 == 0 ){
    print(paste("Leap Year", year))
}else{
    print(paste(" Not Leap Year", year))
}
