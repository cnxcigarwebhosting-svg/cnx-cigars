import styles from './Footer.module.css';

export default function Footer() {
  return (
    <footer className={styles.footer} id="location">
      <div className={styles.container}>
        <div className={styles.col}>
          <h3 className={styles.brand}>CNX <span className={styles.gold}>CIGARS</span></h3>
          <p className={styles.desc}>
            The official licensed & trusted distributor of premium cigar services and accessories to Northern Thailand.
          </p>
        </div>
        
        <div className={styles.col}>
          <h4 className={styles.heading}>Location</h4>
          <p className={styles.text}>
            NPARC (Upstairs)<br />
            45 Nimmanhaemin (Soi 11)<br />
            Tambon Su Thep, Mueang Chiang Mai<br />
            Chiang Mai 50200
          </p>
          <div className={styles.mapContainer}>
            <iframe 
              src="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3777.0605929653835!2d98.9649174154848!3d18.79796038724286!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x30da3a00259e88cb%3A0xbce5c739a859e2ab!2sCNX%20Cigars%20International%20Cigar%20Bar%20and%20lounge!5e0!3m2!1sen!2sth!4v1714777200000!5m2!1sen!2sth" 
              width="100%" 
              height="200" 
              style={{ border: 0, borderRadius: '4px', marginTop: '1rem' }} 
              allowFullScreen={true} 
              loading="lazy" 
              referrerPolicy="no-referrer-when-downgrade"
            ></iframe>
          </div>
        </div>

        <div className={styles.col} id="contact">
          <h4 className={styles.heading}>Contact</h4>
          <p className={styles.text}>
            Whatsapp: +66 622769937<br />
            LINE ID: Bodazey<br />
            Email: cigarschiangmai@gmail.com
          </p>
        </div>
      </div>
      <div className={styles.bottom}>
        <p>&copy; {new Date().getFullYear()} CIGARS CHIANG MAI CO., LTD. All rights reserved.</p>
        <p className={styles.warning}>ONLINE SALE OF TOBACCO IS STRICTLY PROHIBITED IN THE KINGDOM OF THAILAND INCLUDING SALES TO PERSONS UNDER 20 YEARS.</p>
      </div>
    </footer>
  );
}
