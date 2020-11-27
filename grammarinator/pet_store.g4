grammar pet_store;

valid_url: BASE_URL endpoint;

endpoint: pet_endpoint | store_endpoint;

pet_endpoint: '/pet' pet_path;
store_endpoint: '/store' store_path;

pet_path: '/' (pet_id | 'findByStatus?status=' pet_status);
pet_id: INTEGER;
pet_status: 'available' | 'pending' | 'sold';

store_path: '/' ('order/' order_id | 'inventory');
order_id: INTEGER;

BASE_URL: 'https://petstore.swagger.io/v2';

INTEGER: NON_ZERO_DIGIT DIGIT* | '0';
fragment NON_ZERO_DIGIT: [1-9];
fragment DIGIT: [0-9];


