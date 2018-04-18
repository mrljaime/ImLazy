# --*-- encoding: utf-8 --*--

from logger import logging

class PaymentCompanyDao():
     
    def __init__(self, db_manager):
        """
        Use to access into database to search payment_company
        :param stamper.DBManager db_manager
        """
        self.db_manager = db_manager

    def get_by_rfc(self, rfc):
        stmt = (
            "SELECT "
            "   id, "
            "   rfc, "
            "   ws_user, " 
            "   ws_password "
            "FROM payment_company "
            "WHERE rfc = %(rfc)s "
        )
        payment_companies = self.db_manager.select(stmt, {'rfc': rfc})
        for payment_company in payment_companies:
            logging.debug(payment_company)

            return payment_company