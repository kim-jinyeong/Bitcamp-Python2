from icecream import ic
from context.models import Model
from context.domains import Dataset
from sklearn.model_selection import KFold
from sklearn.model_selection import cross_val_score
from sklearn.ensemble import RandomForestClassifier
import pandas as pd
import numpy as np

class TitanicModel(object):
    model = Model()
    dataset = Dataset()

    def preprocess(self, train_fname, test_fname):
        this = self.dataset
        that = self.model
        # 데이터셋은 Train, Test, Validation 3종류
        this.train = that.new_dframe(train_fname)
        this.test = that.new_dframe(test_fname)
        this.id = this.test['PassengerId']
        this.label = this.train['Survived']
        this.train = this.train.drop('Survived', axis=1)
        # Entity 에서 Object 로 전환
        this = self.drop_feature(this, 'Cabin', 'Parch', 'Ticket', 'SibSp')
        #self.kwargs_sample(name='이순신')
        this = self.extract_title_from_name(this)
        title_mapping = self.remove_duplicate(this)
        this = self.title_nominal(this, title_mapping)
        this = self.drop_feature(this, 'Name')
        this = self.sex_nominal(this)
        this = self.drop_feature(this, 'Sex')
        this = self.embarked_nominal(this)
        this = self.age_ratio(this)
        this = self.drop_feature(this, 'Age')
        this = self.fare_ratio(this)
        this = self.drop_feature(this, 'Fare')
        this = self.pclass_ordinal(this)
        #self.print_this(this)
        #self.df_info(this)
        k_fold = self.create_k_fold()
        accuracy = self.get_accuracy(this, k_fold)
        ic(accuracy)
        return this

    @staticmethod
    def df_info(this):
        [print(f'{i.info()}') for i in [this.train, this.test]]
        ic(this.train.head(3))
        ic(this.test.head(3))

    @staticmethod
    def print_this(this):
        print('*' * 100)
        ic(f'1. Train의 타입 {type(this.train)}\n')
        ic(f'2. Train의 컬럼 {this.train.columns}\n')
        ic(f'3. Train의 상위1개 {this.train.head(1)}\n')
        ic(f'4. Train의 null의 개수 {this.train.isnull().sum()}\n')
        ic(f'5. Test의 타입 {type(this.test)}\n')
        ic(f'6. Test의 컬럼 {this.test.columns}\n')
        ic(f'7. Test의 상위1개 {this.test.head(1)}\n')
        ic(f'8. Test의 null의 개수 {this.test.isnull().sum()}\n')
        ic(f'9. id의 타입 :  {type(this.id)}\n')
        ic(f'10. id 의 상위 10개 {this.id[:10]}\n')
        print('*' * 100)
    '''
        nominal(이름) vs ordinal(순서)
        quantitative -> (숫자)
        interval(상대) vs ratio(절대적인기준)
    '''
    @staticmethod
    def drop_feature(this, *feature) -> object:
        [i.drop(j, axis=1, inplace=True) for j in feature for i in [this.train, this.test]]
        #this.train = [this.train.drop(i, axis=1) for i in feature]
        '''
        this.train = this.train.drop('SibSp', axis=1)
        this.train = this.train.drop('Parch', axis=1)
        this.train = this.train.drop('Cabin', axis=1)
        this.train = this.train.drop('Ticket', axis=1)
        '''
        #this.test = [this.test.drop(i, axis=1) for i in feature]
        '''
        this.test = this.test.drop('SibSp', axis=1)
        this.test = this.test.drop('Parch', axis=1)
        this.test = this.test.drop('Cabin', axis=1)
        this.test = this.test.drop('Ticket', axis=1)
        '''
        '''
        self.sibsp_garbage()
        self.parch_garbage()
        self.ticket_garbage()
        self.cabin_garbage()
             survived
        '''
        return this


    @staticmethod
    def kwargs_sample(**kwargs) -> None:
        [print(''.join(f'key:{i}, val:{j}')) for i, j in kwargs.items()] # key:name, val:이순신
        return None

    @staticmethod
    def pclass_ordinal(this) -> object:
        return this

    @staticmethod
    def extract_title_from_name(this) -> None:
        for these in [this.train, this.test]:
            these['Title'] = these.Name.str.extract('([A-Za-z]+)\.', expand=False)
            # ic(this.train.head(5))
        return this

    @staticmethod
    def remove_duplicate(this) -> None:
        a = []
        for dataset in [this.train, this.test]:
            a += list(set(dataset['Title']))
        d = list(set(a))
        #print(f'>>>{a}')
        '''
        ['Mr', 'Sir', 'Major', 'Don', 'Rev', 'Countess', 'Lady', 'Jonkheer', 'Dr',
        'Miss', 'Col', 'Ms', 'Dona', 'Mlle', 'Mme', 'Mrs', 'Master', 'Capt']
        Royal : ['Countess', 'Lady', 'Sir']
        Rare : ['Capt','Col','Don','Dr','Major','Rev','Jonkheer','Dona','Mme' ]
        Mr : ['Mlle']
        Ms : ['Miss']
        Master
        Mrs
        '''
        title_mapping = {'Mr': 1, 'Ms': 2, 'Mrs': 3, 'Master': 4, 'Royal': 5, 'Rare': 6}
        return title_mapping

    @staticmethod
    def title_nominal(this, title_mapping) -> object:
        for these in [this.train, this.test]:
            these['Title'] = these['Title'].replace(['Countess', 'Lady', 'Sir'], 'Royal')
            these['Title'] = these['Title'].replace(['Capt', 'Col', 'Don', 'Dr', 'Major', 'Rev', 'Jonkheer', 'Dona', 'Mme'], 'Rare')
            these['Title'] = these['Title'].replace(['Mlle'], 'Mr')
            these['Title'] = these['Title'].replace(['Miss'], 'Ms')
            # Master 는 변화없음
            # Mrs 는 변화없음
            these['Title'] = these['Title'].fillna(0)
            these['Title'] = these['Title'].map(title_mapping)
        return this

    @staticmethod
    def sex_nominal(this) -> object:
        gender_mapping = {'male': 0, 'female': 1}
        for these in [this.train, this.test]:
            these['Gender'] = these['Sex'].map(gender_mapping)
        return this

    @staticmethod
    def age_ratio(this) -> object:
        train = this.train
        test = this.test
        age_mapping = {'Unknown': 0, 'Baby': 1, 'Child': 2, 'Teenager' : 3, 'Student': 4,
                       'Young Adult': 5, 'Adult': 6,  'Senior': 7}
        bins = [-1, 0, 5, 12, 18, 24, 35, 60, np.inf]
        labels = ['Unknown', 'Baby', 'Child', 'Teenager', 'Student', 'Young Adult', 'Adult', 'Senior']
        for these in train, test:
            these['Age'] = these['Age'].fillna(-0.5)
            # pd.cut() 을 사용하시오. 다른 곳은 고치지 말고 다음 두 줄만 코딩하시오
            these['AgeGroup'] = pd.cut(these['Age'], bins, labels=labels)# pd.cut() 을 사용
            these['AgeGroup'] = these['AgeGroup'].map(age_mapping) # map() 을 사용
        return this

    @staticmethod
    def fare_ratio(this) -> object:
        train = this.train
        test = this.test
        fare_mapping = {1, 2, 3, 4}
        bins = [-1, 8, 15, 31, np.inf]
        for these in [train, test]:
            these['Fare'] = these['Fare'].fillna(1)
            these['FareBand'] = pd.qcut(these['Fare'], 4, labels=fare_mapping)
        return this

    @staticmethod
    def embarked_nominal(this) -> object:
        embarked_mapping = {'S': 1, 'C': 2, 'Q': 3}
        this.train = this.train.fillna({'Embarked': 'S'})
        for these in [this.train, this.test]:
            these['Embarked'] = these['Embarked'].map(embarked_mapping)
        return this

    @staticmethod
    def create_k_fold() -> object:
        return KFold(n_splits=10, shuffle=True, random_state=0)

    @staticmethod
    def get_accuracy(this, k_fold):
        score = cross_val_score(RandomForestClassifier(), this.train, this.label, cv=k_fold,  n_jobs=1, scoring='accuracy')
        return round(np.mean(score)*100, 2)
