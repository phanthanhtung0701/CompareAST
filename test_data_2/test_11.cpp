int getDay(int day){
    switch (day) {
          case 6:
                cout << "Today is Saturday";
                break;
          case 7:
                cout << "Today is Sunday";
                break;
          default:
                cout << "Looking forward to the Weekend";
    }

    return 0;
}

void main(){
    int day = 4;
    getDay(day);
}