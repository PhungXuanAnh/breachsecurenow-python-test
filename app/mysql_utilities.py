import pymysql
import pymysql.cursors

create_table_customer_sql = """
CREATE TABLE IF NOT EXISTS `customers` (
    `id` int(11) NOT NULL AUTO_INCREMENT,
    `email` varchar(255) COLLATE utf8_bin NOT NULL UNIQUE,
    `name` varchar(50) COLLATE utf8_bin NOT NULL,
    PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_bin
AUTO_INCREMENT=1 ;
"""

create_table_vehicle_sql = """
CREATE TABLE IF NOT EXISTS `vehicles` (
    `id` int(11) NOT NULL AUTO_INCREMENT,
    `type` int(11) NOT NULL,
    `is_available` boolean NOT NULL,
    PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_bin
AUTO_INCREMENT=1 ;
"""

create_table_booking_sql = """
CREATE TABLE IF NOT EXISTS `bookings` (
    `id` int(11) NOT NULL AUTO_INCREMENT,
    `customer_id` int(11),
    `vehicle_id` int(11),
    `hired_date` datetime NOT NULL,
    `returned_date` datetime NOT NULL,
    `is_paid` boolean NOT NULL,
    PRIMARY KEY (`id`),
    FOREIGN KEY (`customer_id`) REFERENCES customers(`id`)
        ON DELETE SET NULL
        ON UPDATE CASCADE,
    FOREIGN KEY (`vehicle_id`) REFERENCES vehicles(`id`)
        ON DELETE SET NULL
        ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_bin
AUTO_INCREMENT=1 ;
"""

connection = pymysql.connect(
    host="localhost",
    user="user",
    password="passwd",
    database="db",
    cursorclass=pymysql.cursors.DictCursor,
)


def create_tables():
    with connection:
        with connection.cursor() as cursor:
            cursor.execute(create_table_customer_sql)
            cursor.execute(create_table_vehicle_sql)
            cursor.execute(create_table_booking_sql)

def create_customer_data(email, name):
    with connection.cursor() as cursor:
        sql = "INSERT INTO `customers` (`email`, `name`) VALUES (%s, %s)"
        cursor.execute(sql, (email, name))
    connection.commit()


def update_customer_data(customer_id, email, name):
    with connection.cursor() as cursor:
        sql = "UPDATE `customers` SET email=%s, name=%s WHERE `id`=%s"
        cursor.execute(sql, (email, name, customer_id))
    connection.commit()


def get_customer_data(customer_id=None, email=None):
    with connection.cursor() as cursor:

        if email:
            cursor.execute(
                "SELECT `id`, `email`, `name` FROM `customers` WHERE `email`=%s",
                (email,),
            )
            return cursor.fetchone()
        if customer_id:
            cursor.execute(
                "SELECT `id`, `email`, `name` FROM `customers` WHERE `id`=%s",
                (customer_id,),
            )
            return cursor.fetchone()
        return None


def delete_customer_data(customer_id=None, email=None):
    with connection.cursor() as cursor:
        if customer_id:
            cursor.execute("DELETE FROM `customers` WHERE `id`=%s", (customer_id,))
        if email:
            cursor.execute("DELETE FROM `customers` WHERE `email`=%s", (email,))
    connection.commit()


if __name__ == "__main__":
    # create_tables()
    
    # create_customer("test@gmail.com", "Alexander")
    # print(get_customer(email="test@gmail.com"))
    
    # update_customer_data(1, "test1@gmail.com", "Alexander1")
    # print(get_customer(email="test@gmail.com"))
    # print(get_customer(customer_id=1))
    
    delete_customer_data(3)
    print(get_customer_data(customer_id=3))
    pass