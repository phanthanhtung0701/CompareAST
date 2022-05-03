#include <bits/stdc++.h>
using namespace std;

int n,k;
bool check_continue = true;
vector<string> ans;

bool isOk(string s){
	for(int i=0;i<s.length();i++){
		if(s[i]!=s[s.length()-i-1]) return false;
	}
	return true;
}

void next_binary(string &s){
	if(isOk(s)){
		ans.push_back(s);
	}
	int pos=s.length()-1;
	while(pos>= 0 && s[pos]=='1'){
		s[pos]='0';
		pos--;
	}
	if(pos == -1){
		check_continue = false;
		return;
	}
	s[pos]='1';
}

void solve(){
	cin>> n;
	string s;
	for(int i=0;i<n;i++) s+='0';
	while(check_continue == true){
		next_binary(s);
	}
	for(int i=0;i<ans.size();i++){
		s=ans[i];
		for(int i=0;i<s.length();i++){
		   cout<< s[i]<< " ";
		}
		cout<<endl;
	}
}

int main(){
	int t=1;
	while(t--) solve();
}
