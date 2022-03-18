from icecream import ic
from context.models import Model
from context.domains import Dataset


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
        self.kwargs_sample(name='이순신')
        '''
        this = self.create_train(this)
        this = self.create_label(this)
        this = self.name_nominal(this)  
        this = self.sex_nominal(this)
        this = self.age_ratio(this)
        this = self.embarked_nominal(this)
        this = self.pclass_ordinal(this)
        this = self.fare_ratio(this)
        '''
        self.print_this(this)
        return this

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

    def create_this(self, dataset) -> object:
        this = dataset
        this.train = self.train
        this.tset = self.test
        this.id = self.id
        return this

    @staticmethod
    def create_label(this) -> object:
        return this

    @staticmethod
    def create_train(this) -> object:
        return this

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
    def name_nominal(this) -> object:
        return this

    @staticmethod
    def sex_nominal(this) -> object:
        return this

    @staticmethod
    def age_ratio(this) -> object:
        return this

    @staticmethod
    def fare_ratio(this) -> object:
        return this

    @staticmethod
    def embarked_nominal(this) -> object:
        return this