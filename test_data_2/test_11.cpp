void getDay(int day){
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
}

void main(){
    int day = 4;
    getDay(day);
}
