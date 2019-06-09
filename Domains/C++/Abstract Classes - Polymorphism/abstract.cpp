#include <iostream>
#include <vector>
#include <map>
#include <string>
#include <algorithm>
#include <set>
#include <cassert>
using namespace std;

struct Node{
   Node* next;
   Node* prev;
   int value;
   int key;
   Node(Node* p, Node* n, int k, int val):prev(p),next(n),key(k),value(val){};
   Node(int k, int val):prev(NULL),next(NULL),key(k),value(val){};
};

class Cache{

   protected:
   map<int,Node*> mp; //map the key to the node in the linked list
   int cp;  //capacity
   Node* tail; // double linked list tail pointer
   Node* head; // double linked list head pointer
   virtual void set(int, int) = 0; //set function
   virtual int get(int) = 0; //get function

};

//------------------------------------------------------------------------------

class LRUCache: public Cache{
    private:
        Node * ptr, *lastPtr, *temp;
        map<int, Node*>::iterator itr, end;
    public:
        LRUCache(int cap);
        void display();
        void set(int, int);
        int get(int);
};

LRUCache :: LRUCache(int cap){
    cp = cap;
}

void LRUCache :: set(int k, int v){
    cout<<"!!";
    ptr = NULL;
    itr = mp.find(k);
    if(itr == mp.end()){                //element not found, insert a new element
        cout<<"Not Found! Creating new one!";
        if(mp.size() >= cp){            //if current size is equal to or greater than cp delete tail
            cout<<"!!";
                temp = tail;
            if(tail->next != NULL){
                tail = tail->next;
            }else{
                head = tail = NULL;
            }
            mp.erase(mp.find(temp->key));
            delete temp;
        }

        if(mp.size() == 0){             //if no element exists create new
            head = new Node(NULL, NULL, k, v);
            tail = head;
            mp[k] = head;
        }else{
            ptr = NULL;
            temp = head;
            ptr = new Node(head, NULL, k, v);
            head = ptr;
            temp->next = head;
            lastPtr = ptr;

            if(tail == NULL){
                tail == ptr;
            }
            mp[k] = ptr;
        }
    }else{
        cout<<"Element Found in the list!!";
        ptr = itr->second;

        if(mp.size() >= cp){            //if current size is equal to or greater than cp delete tail
            cout<<"!!";
            temp = tail;
            if(tail->next != NULL){
                tail = tail->next;
            }else{
                head = tail = NULL;
            }
            mp.erase(mp.find(temp->key));
            delete temp;
        }

        if(v == ptr->value){
            if(ptr != head){

                if(ptr->prev != NULL){
                    temp = ptr->prev;
                    temp->next = ptr->next;
                    ptr->next = NULL;
                }

                temp = head;
                temp->next = ptr;
                ptr->prev = temp;
                head = ptr;
            }
        }else{
            ptr->value = v;

            if(ptr != head){
                if(mp.size() > 1){
                    temp = head;
                    head->next = ptr;
                    head->prev = ptr->prev;
                    ptr->prev = head;
                    head = ptr;
                    head->next = NULL;
                }
            }
            if(head == NULL){
                tail = head = mp[k] = new Node(NULL, NULL, k, v);
            }
        }
    }
}

int LRUCache :: get(int k){
    itr = mp.find(k);

    if(itr != mp.end()){
        ptr = mp[k];
        // cout<<"get: found!";

        return ptr->value;
    }

    return -1;
}

//------------------------------------------------------------------------------

void LRUCache :: display(){
    cout<<"\nMap Contents are:\t";
    for(itr=mp.begin(), end=mp.end(); itr!=end; ++itr){
        cout<<itr->second->value<<" ";
    }
    cout<<"\n";
}

int main() {
   int n, capacity,i;
   cin >> n >> capacity;
   LRUCache l(capacity);
   for(i=0;i<n;i++) {
      string command;
      cin >> command;
      if(command == "get") {
         int key;
         cin >> key;
         cout << l.get(key) << endl;
      }
      else if(command == "set") {
         int key, value;
         cin >> key >> value;
         l.set(key,value);
      }
      l.display();
   }
   return 0;
}
