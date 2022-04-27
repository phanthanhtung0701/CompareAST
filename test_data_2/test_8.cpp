void func3(n){
    if ( n == 0 ) {
        return;
    }
}


boolean debug = false ;
void func4(n){
    if ( n == 0 ) {
        if(debug){
            cout << "ERROR: ...";
        }
        return;
    }
}
