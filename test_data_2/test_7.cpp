struct person
{ 
  char name[60]; 
  short age;
};

struct worker
{ 
  struct person peronal_ID;
  char job[30];
  float income;
};