# Generated by Django 2.0.2 on 2018-03-10 14:14

from django.db import migrations
import separatedvaluesfield.models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_auto_20180309_0302'),
    ]

    operations = [
        migrations.AlterField(
            model_name='designdocument',
            name='typefaces',
            field=separatedvaluesfield.models.SeparatedValuesField(blank=True, choices=[('Agipo', 'agipo'), ('Akkurat', 'akkurat'), ('Akzidenz-Grotesk Pro', 'akzidenz-grotesk_pro'), ('Antwerp', 'antwerp'), ('ABeeZee', 'abeezee'), ('Abel', 'abel'), ('Abhaya Libre', 'abhaya_libre'), ('Abril Fatface', 'abril_fatface'), ('Aclonica', 'aclonica'), ('Acme', 'acme'), ('Actor', 'actor'), ('Adamina', 'adamina'), ('Advent Pro', 'advent_pro'), ('Aguafina Script', 'aguafina_script'), ('Akronim', 'akronim'), ('Aladin', 'aladin'), ('Aldrich', 'aldrich'), ('Alef', 'alef'), ('Alegreya', 'alegreya'), ('Alegreya SC', 'alegreya_sc'), ('Alegreya Sans', 'alegreya_sans'), ('Alegreya Sans SC', 'alegreya_sans_sc'), ('Alex Brush', 'alex_brush'), ('Alfa Slab One', 'alfa_slab_one'), ('Alice', 'alice'), ('Alike', 'alike'), ('Alike Angular', 'alike_angular'), ('Allan', 'allan'), ('Allerta', 'allerta'), ('Allerta Stencil', 'allerta_stencil'), ('Allura', 'allura'), ('Almendra', 'almendra'), ('Almendra Display', 'almendra_display'), ('Almendra SC', 'almendra_sc'), ('Amarante', 'amarante'), ('Amaranth', 'amaranth'), ('Amatic SC', 'amatic_sc'), ('Amethysta', 'amethysta'), ('Amiko', 'amiko'), ('Amiri', 'amiri'), ('Amita', 'amita'), ('Anaheim', 'anaheim'), ('Andada', 'andada'), ('Andika', 'andika'), ('Angkor', 'angkor'), ('Annie Use Your Telescope', 'annie_use_your_telescope'), ('Anonymous Pro', 'anonymous_pro'), ('Antic', 'antic'), ('Antic Didone', 'antic_didone'), ('Antic Slab', 'antic_slab'), ('Anton', 'anton'), ('Arapey', 'arapey'), ('Arbutus', 'arbutus'), ('Arbutus Slab', 'arbutus_slab'), ('Architects Daughter', 'architects_daughter'), ('Archivo', 'archivo'), ('Archivo Black', 'archivo_black'), ('Archivo Narrow', 'archivo_narrow'), ('Aref Ruqaa', 'aref_ruqaa'), ('Arima Madurai', 'arima_madurai'), ('Arimo', 'arimo'), ('Arizonia', 'arizonia'), ('Armata', 'armata'), ('Arsenal', 'arsenal'), ('Artifika', 'artifika'), ('Arvo', 'arvo'), ('Arya', 'arya'), ('Asap', 'asap'), ('Asap Condensed', 'asap_condensed'), ('Asar', 'asar'), ('Asset', 'asset'), ('Assistant', 'assistant'), ('Astloch', 'astloch'), ('Asul', 'asul'), ('Athiti', 'athiti'), ('Atma', 'atma'), ('Atomic Age', 'atomic_age'), ('Aubrey', 'aubrey'), ('Audiowide', 'audiowide'), ('Autour One', 'autour_one'), ('Average', 'average'), ('Average Sans', 'average_sans'), ('Averia Gruesa Libre', 'averia_gruesa_libre'), ('Averia Libre', 'averia_libre'), ('Averia Sans Libre', 'averia_sans_libre'), ('Averia Serif Libre', 'averia_serif_libre'), ('Bad Script', 'bad_script'), ('Bahiana', 'bahiana'), ('Baloo', 'baloo'), ('Baloo Bhai', 'baloo_bhai'), ('Baloo Bhaijaan', 'baloo_bhaijaan'), ('Baloo Bhaina', 'baloo_bhaina'), ('Baloo Chettan', 'baloo_chettan'), ('Baloo Da', 'baloo_da'), ('Baloo Paaji', 'baloo_paaji'), ('Baloo Tamma', 'baloo_tamma'), ('Baloo Tammudu', 'baloo_tammudu'), ('Baloo Thambi', 'baloo_thambi'), ('Balthazar', 'balthazar'), ('Bangers', 'bangers'), ('Barlow', 'barlow'), ('Barlow Condensed', 'barlow_condensed'), ('Barlow Semi Condensed', 'barlow_semi_condensed'), ('Barrio', 'barrio'), ('Basic', 'basic'), ('Battambang', 'battambang'), ('Baumans', 'baumans'), ('Bayon', 'bayon'), ('Belgrano', 'belgrano'), ('Bellefair', 'bellefair'), ('Belleza', 'belleza'), ('BenchNine', 'benchnine'), ('Bentham', 'bentham'), ('Berkshire Swash', 'berkshire_swash'), ('Bevan', 'bevan'), ('Bigelow Rules', 'bigelow_rules'), ('Bigshot One', 'bigshot_one'), ('Bilbo', 'bilbo'), ('Bilbo Swash Caps', 'bilbo_swash_caps'), ('BioRhyme', 'biorhyme'), ('BioRhyme Expanded', 'biorhyme_expanded'), ('Biryani', 'biryani'), ('Bitter', 'bitter'), ('Black Ops One', 'black_ops_one'), ('Bokor', 'bokor'), ('Bonbon', 'bonbon'), ('Boogaloo', 'boogaloo'), ('Bowlby One', 'bowlby_one'), ('Bowlby One SC', 'bowlby_one_sc'), ('Brawler', 'brawler'), ('Bree Serif', 'bree_serif'), ('Bubblegum Sans', 'bubblegum_sans'), ('Bubbler One', 'bubbler_one'), ('Buda', 'buda'), ('Buenard', 'buenard'), ('Bungee', 'bungee'), ('Bungee Hairline', 'bungee_hairline'), ('Bungee Inline', 'bungee_inline'), ('Bungee Outline', 'bungee_outline'), ('Bungee Shade', 'bungee_shade'), ('Butcherman', 'butcherman'), ('Butterfly Kids', 'butterfly_kids'), ('Cabin', 'cabin'), ('Cabin Condensed', 'cabin_condensed'), ('Cabin Sketch', 'cabin_sketch'), ('Caesar Dressing', 'caesar_dressing'), ('Cagliostro', 'cagliostro'), ('Cairo', 'cairo'), ('Calligraffitti', 'calligraffitti'), ('Cambay', 'cambay'), ('Cambo', 'cambo'), ('Candal', 'candal'), ('Cantarell', 'cantarell'), ('Cantata One', 'cantata_one'), ('Cantora One', 'cantora_one'), ('Capriola', 'capriola'), ('Cardo', 'cardo'), ('Carme', 'carme'), ('Carrois Gothic', 'carrois_gothic'), ('Carrois Gothic SC', 'carrois_gothic_sc'), ('Carter One', 'carter_one'), ('Catamaran', 'catamaran'), ('Caudex', 'caudex'), ('Caveat', 'caveat'), ('Caveat Brush', 'caveat_brush'), ('Cedarville Cursive', 'cedarville_cursive'), ('Ceviche One', 'ceviche_one'), ('Changa', 'changa'), ('Changa One', 'changa_one'), ('Chango', 'chango'), ('Chathura', 'chathura'), ('Chau Philomene One', 'chau_philomene_one'), ('Chela One', 'chela_one'), ('Chelsea Market', 'chelsea_market'), ('Chenla', 'chenla'), ('Cherry Cream Soda', 'cherry_cream_soda'), ('Cherry Swash', 'cherry_swash'), ('Chewy', 'chewy'), ('Chicle', 'chicle'), ('Chivo', 'chivo'), ('Chonburi', 'chonburi'), ('Cinzel', 'cinzel'), ('Cinzel Decorative', 'cinzel_decorative'), ('Clicker Script', 'clicker_script'), ('Coda', 'coda'), ('Coda Caption', 'coda_caption'), ('Codystar', 'codystar'), ('Coiny', 'coiny'), ('Combo', 'combo'), ('Comfortaa', 'comfortaa'), ('Coming Soon', 'coming_soon'), ('Concert One', 'concert_one'), ('Condiment', 'condiment'), ('Content', 'content'), ('Contrail One', 'contrail_one'), ('Convergence', 'convergence'), ('Cookie', 'cookie'), ('Copse', 'copse'), ('Corben', 'corben'), ('Cormorant', 'cormorant'), ('Cormorant Garamond', 'cormorant_garamond'), ('Cormorant Infant', 'cormorant_infant'), ('Cormorant SC', 'cormorant_sc'), ('Cormorant Unicase', 'cormorant_unicase'), ('Cormorant Upright', 'cormorant_upright'), ('Courgette', 'courgette'), ('Cousine', 'cousine'), ('Coustard', 'coustard'), ('Covered By Your Grace', 'covered_by_your_grace'), ('Crafty Girls', 'crafty_girls'), ('Creepster', 'creepster'), ('Crete Round', 'crete_round'), ('Crimson Text', 'crimson_text'), ('Croissant One', 'croissant_one'), ('Crushed', 'crushed'), ('Cuprum', 'cuprum'), ('Cutive', 'cutive'), ('Cutive Mono', 'cutive_mono'), ('Damion', 'damion'), ('Dancing Script', 'dancing_script'), ('Dangrek', 'dangrek'), ('David Libre', 'david_libre'), ('Dawning of a New Day', 'dawning_of_a_new_day'), ('Days One', 'days_one'), ('Dekko', 'dekko'), ('Delius', 'delius'), ('Delius Swash Caps', 'delius_swash_caps'), ('Delius Unicase', 'delius_unicase'), ('Della Respira', 'della_respira'), ('Denk One', 'denk_one'), ('Devonshire', 'devonshire'), ('Dhurjati', 'dhurjati'), ('Didact Gothic', 'didact_gothic'), ('Diplomata', 'diplomata'), ('Diplomata SC', 'diplomata_sc'), ('Domine', 'domine'), ('Donegal One', 'donegal_one'), ('Doppio One', 'doppio_one'), ('Dorsa', 'dorsa'), ('Dosis', 'dosis'), ('Dr Sugiyama', 'dr_sugiyama'), ('Duru Sans', 'duru_sans'), ('Dynalight', 'dynalight'), ('EB Garamond', 'eb_garamond'), ('Eagle Lake', 'eagle_lake'), ('Eater', 'eater'), ('Economica', 'economica'), ('Eczar', 'eczar'), ('El Messiri', 'el_messiri'), ('Electrolize', 'electrolize'), ('Elsie', 'elsie'), ('Elsie Swash Caps', 'elsie_swash_caps'), ('Emblema One', 'emblema_one'), ('Emilys Candy', 'emilys_candy'), ('Encode Sans', 'encode_sans'), ('Encode Sans Condensed', 'encode_sans_condensed'), ('Encode Sans Expanded', 'encode_sans_expanded'), ('Encode Sans Semi Condensed', 'encode_sans_semi_condensed'), ('Encode Sans Semi Expanded', 'encode_sans_semi_expanded'), ('Engagement', 'engagement'), ('Englebert', 'englebert'), ('Enriqueta', 'enriqueta'), ('Erica One', 'erica_one'), ('Esteban', 'esteban'), ('Euphoria Script', 'euphoria_script'), ('Ewert', 'ewert'), ('Exo', 'exo'), ('Exo 2', 'exo_2'), ('Expletus Sans', 'expletus_sans'), ('Fanwood Text', 'fanwood_text'), ('Farsan', 'farsan'), ('Fascinate', 'fascinate'), ('Fascinate Inline', 'fascinate_inline'), ('Faster One', 'faster_one'), ('Fasthand', 'fasthand'), ('Fauna One', 'fauna_one'), ('Faustina', 'faustina'), ('Federant', 'federant'), ('Federo', 'federo'), ('Felipa', 'felipa'), ('Fenix', 'fenix'), ('Finger Paint', 'finger_paint'), ('Fira Mono', 'fira_mono'), ('Fira Sans', 'fira_sans'), ('Fira Sans Condensed', 'fira_sans_condensed'), ('Fira Sans Extra Condensed', 'fira_sans_extra_condensed'), ('Fjalla One', 'fjalla_one'), ('Fjord One', 'fjord_one'), ('Flamenco', 'flamenco'), ('Flavors', 'flavors'), ('Fondamento', 'fondamento'), ('Fontdiner Swanky', 'fontdiner_swanky'), ('Forum', 'forum'), ('Francois One', 'francois_one'), ('Frank Ruhl Libre', 'frank_ruhl_libre'), ('Freckle Face', 'freckle_face'), ('Fredericka the Great', 'fredericka_the_great'), ('Fredoka One', 'fredoka_one'), ('Freehand', 'freehand'), ('Fresca', 'fresca'), ('Frijole', 'frijole'), ('Fruktur', 'fruktur'), ('Fugaz One', 'fugaz_one'), ('GFS Didot', 'gfs_didot'), ('GFS Neohellenic', 'gfs_neohellenic'), ('Gabriela', 'gabriela'), ('Gafata', 'gafata'), ('Galada', 'galada'), ('Galdeano', 'galdeano'), ('Galindo', 'galindo'), ('Gentium Basic', 'gentium_basic'), ('Gentium Book Basic', 'gentium_book_basic'), ('Geo', 'geo'), ('Geostar', 'geostar'), ('Geostar Fill', 'geostar_fill'), ('Germania One', 'germania_one'), ('Gidugu', 'gidugu'), ('Gilda Display', 'gilda_display'), ('Give You Glory', 'give_you_glory'), ('Glass Antiqua', 'glass_antiqua'), ('Glegoo', 'glegoo'), ('Gloria Hallelujah', 'gloria_hallelujah'), ('Goblin One', 'goblin_one'), ('Gochi Hand', 'gochi_hand'), ('Gorditas', 'gorditas'), ('Goudy Bookletter 1911', 'goudy_bookletter_1911'), ('Graduate', 'graduate'), ('Grand Hotel', 'grand_hotel'), ('Gravitas One', 'gravitas_one'), ('Great Vibes', 'great_vibes'), ('Griffy', 'griffy'), ('Gruppo', 'gruppo'), ('Gudea', 'gudea'), ('Gurajada', 'gurajada'), ('Habibi', 'habibi'), ('Halant', 'halant'), ('Hammersmith One', 'hammersmith_one'), ('Hanalei', 'hanalei'), ('Hanalei Fill', 'hanalei_fill'), ('Handlee', 'handlee'), ('Hanuman', 'hanuman'), ('Happy Monkey', 'happy_monkey'), ('Harmattan', 'harmattan'), ('Headland One', 'headland_one'), ('Heebo', 'heebo'), ('Henny Penny', 'henny_penny'), ('Herr Von Muellerhoff', 'herr_von_muellerhoff'), ('Hind', 'hind'), ('Hind Guntur', 'hind_guntur'), ('Hind Madurai', 'hind_madurai'), ('Hind Siliguri', 'hind_siliguri'), ('Hind Vadodara', 'hind_vadodara'), ('Holtwood One SC', 'holtwood_one_sc'), ('Homemade Apple', 'homemade_apple'), ('Homenaje', 'homenaje'), ('IM Fell DW Pica', 'im_fell_dw_pica'), ('IM Fell DW Pica SC', 'im_fell_dw_pica_sc'), ('IM Fell Double Pica', 'im_fell_double_pica'), ('IM Fell Double Pica SC', 'im_fell_double_pica_sc'), ('IM Fell English', 'im_fell_english'), ('IM Fell English SC', 'im_fell_english_sc'), ('IM Fell French Canon', 'im_fell_french_canon'), ('IM Fell French Canon SC', 'im_fell_french_canon_sc'), ('IM Fell Great Primer', 'im_fell_great_primer'), ('IM Fell Great Primer SC', 'im_fell_great_primer_sc'), ('Iceberg', 'iceberg'), ('Iceland', 'iceland'), ('Imprima', 'imprima'), ('Inconsolata', 'inconsolata'), ('Inder', 'inder'), ('Indie Flower', 'indie_flower'), ('Inika', 'inika'), ('Inknut Antiqua', 'inknut_antiqua'), ('Irish Grover', 'irish_grover'), ('Istok Web', 'istok_web'), ('Italiana', 'italiana'), ('Italianno', 'italianno'), ('Itim', 'itim'), ('Jacques Francois', 'jacques_francois'), ('Jacques Francois Shadow', 'jacques_francois_shadow'), ('Jaldi', 'jaldi'), ('Jim Nightshade', 'jim_nightshade'), ('Jockey One', 'jockey_one'), ('Jolly Lodger', 'jolly_lodger'), ('Jomhuria', 'jomhuria'), ('Josefin Sans', 'josefin_sans'), ('Josefin Slab', 'josefin_slab'), ('Joti One', 'joti_one'), ('Judson', 'judson'), ('Julee', 'julee'), ('Julius Sans One', 'julius_sans_one'), ('Junge', 'junge'), ('Jura', 'jura'), ('Just Another Hand', 'just_another_hand'), ('Just Me Again Down Here', 'just_me_again_down_here'), ('Kadwa', 'kadwa'), ('Kalam', 'kalam'), ('Kameron', 'kameron'), ('Kanit', 'kanit'), ('Kantumruy', 'kantumruy'), ('Karla', 'karla'), ('Karma', 'karma'), ('Katibeh', 'katibeh'), ('Kaushan Script', 'kaushan_script'), ('Kavivanar', 'kavivanar'), ('Kavoon', 'kavoon'), ('Kdam Thmor', 'kdam_thmor'), ('Keania One', 'keania_one'), ('Kelly Slab', 'kelly_slab'), ('Kenia', 'kenia'), ('Khand', 'khand'), ('Khmer', 'khmer'), ('Khula', 'khula'), ('Kite One', 'kite_one'), ('Knewave', 'knewave'), ('Kotta One', 'kotta_one'), ('Koulen', 'koulen'), ('Kranky', 'kranky'), ('Kreon', 'kreon'), ('Kristi', 'kristi'), ('Krona One', 'krona_one'), ('Kumar One', 'kumar_one'), ('Kumar One Outline', 'kumar_one_outline'), ('Kurale', 'kurale'), ('La Belle Aurore', 'la_belle_aurore'), ('Laila', 'laila'), ('Lakki Reddy', 'lakki_reddy'), ('Lalezar', 'lalezar'), ('Lancelot', 'lancelot'), ('Lateef', 'lateef'), ('Lato', 'lato'), ('League Script', 'league_script'), ('Leckerli One', 'leckerli_one'), ('Ledger', 'ledger'), ('Lekton', 'lekton'), ('Lemon', 'lemon'), ('Lemonada', 'lemonada'), ('Libre Barcode 128', 'libre_barcode_128'), ('Libre Barcode 128 Text', 'libre_barcode_128_text'), ('Libre Barcode 39', 'libre_barcode_39'), ('Libre Barcode 39 Extended', 'libre_barcode_39_extended'), ('Libre Barcode 39 Extended Text', 'libre_barcode_39_extended_text'), ('Libre Barcode 39 Text', 'libre_barcode_39_text'), ('Libre Baskerville', 'libre_baskerville'), ('Libre Franklin', 'libre_franklin'), ('Life Savers', 'life_savers'), ('Lilita One', 'lilita_one'), ('Lily Script One', 'lily_script_one'), ('Limelight', 'limelight'), ('Linden Hill', 'linden_hill'), ('Lobster', 'lobster'), ('Lobster Two', 'lobster_two'), ('Londrina Outline', 'londrina_outline'), ('Londrina Shadow', 'londrina_shadow'), ('Londrina Sketch', 'londrina_sketch'), ('Londrina Solid', 'londrina_solid'), ('Lora', 'lora'), ('Love Ya Like A Sister', 'love_ya_like_a_sister'), ('Loved by the King', 'loved_by_the_king'), ('Lovers Quarrel', 'lovers_quarrel'), ('Luckiest Guy', 'luckiest_guy'), ('Lusitana', 'lusitana'), ('Lustria', 'lustria'), ('Macondo', 'macondo'), ('Macondo Swash Caps', 'macondo_swash_caps'), ('Mada', 'mada'), ('Magra', 'magra'), ('Maiden Orange', 'maiden_orange'), ('Maitree', 'maitree'), ('Mako', 'mako'), ('Mallanna', 'mallanna'), ('Mandali', 'mandali'), ('Manuale', 'manuale'), ('Marcellus', 'marcellus'), ('Marcellus SC', 'marcellus_sc'), ('Marck Script', 'marck_script'), ('Margarine', 'margarine'), ('Marko One', 'marko_one'), ('Marmelad', 'marmelad'), ('Martel', 'martel'), ('Martel Sans', 'martel_sans'), ('Marvel', 'marvel'), ('Mate', 'mate'), ('Mate SC', 'mate_sc'), ('Maven Pro', 'maven_pro'), ('McLaren', 'mclaren'), ('Meddon', 'meddon'), ('MedievalSharp', 'medievalsharp'), ('Medula One', 'medula_one'), ('Meera Inimai', 'meera_inimai'), ('Megrim', 'megrim'), ('Meie Script', 'meie_script'), ('Merienda', 'merienda'), ('Merienda One', 'merienda_one'), ('Merriweather', 'merriweather'), ('Merriweather Sans', 'merriweather_sans'), ('Metal', 'metal'), ('Metal Mania', 'metal_mania'), ('Metamorphous', 'metamorphous'), ('Metrophobic', 'metrophobic'), ('Michroma', 'michroma'), ('Milonga', 'milonga'), ('Miltonian', 'miltonian'), ('Miltonian Tattoo', 'miltonian_tattoo'), ('Mina', 'mina'), ('Miniver', 'miniver'), ('Miriam Libre', 'miriam_libre'), ('Mirza', 'mirza'), ('Miss Fajardose', 'miss_fajardose'), ('Mitr', 'mitr'), ('Modak', 'modak'), ('Modern Antiqua', 'modern_antiqua'), ('Mogra', 'mogra'), ('Molengo', 'molengo'), ('Molle', 'molle'), ('Monda', 'monda'), ('Monofett', 'monofett'), ('Monoton', 'monoton'), ('Monsieur La Doulaise', 'monsieur_la_doulaise'), ('Montaga', 'montaga'), ('Montez', 'montez'), ('Montserrat', 'montserrat'), ('Montserrat Alternates', 'montserrat_alternates'), ('Montserrat Subrayada', 'montserrat_subrayada'), ('Moul', 'moul'), ('Moulpali', 'moulpali'), ('Mountains of Christmas', 'mountains_of_christmas'), ('Mouse Memoirs', 'mouse_memoirs'), ('Mr Bedfort', 'mr_bedfort'), ('Mr Dafoe', 'mr_dafoe'), ('Mr De Haviland', 'mr_de_haviland'), ('Mrs Saint Delafield', 'mrs_saint_delafield'), ('Mrs Sheppards', 'mrs_sheppards'), ('Mukta', 'mukta'), ('Mukta Mahee', 'mukta_mahee'), ('Mukta Malar', 'mukta_malar'), ('Mukta Vaani', 'mukta_vaani'), ('Muli', 'muli'), ('Mystery Quest', 'mystery_quest'), ('NTR', 'ntr'), ('Nanum Brush Script', 'nanum_brush_script'), ('Nanum Gothic', 'nanum_gothic'), ('Nanum Gothic Coding', 'nanum_gothic_coding'), ('Nanum Myeongjo', 'nanum_myeongjo'), ('Nanum Pen Script', 'nanum_pen_script'), ('Neucha', 'neucha'), ('Neuton', 'neuton'), ('New Rocker', 'new_rocker'), ('News Cycle', 'news_cycle'), ('Niconne', 'niconne'), ('Nixie One', 'nixie_one'), ('Nobile', 'nobile'), ('Nokora', 'nokora'), ('Norican', 'norican'), ('Nosifer', 'nosifer'), ('Nothing You Could Do', 'nothing_you_could_do'), ('Noticia Text', 'noticia_text'), ('Noto Sans', 'noto_sans'), ('Noto Serif', 'noto_serif'), ('Nova Cut', 'nova_cut'), ('Nova Flat', 'nova_flat'), ('Nova Mono', 'nova_mono'), ('Nova Oval', 'nova_oval'), ('Nova Round', 'nova_round'), ('Nova Script', 'nova_script'), ('Nova Slim', 'nova_slim'), ('Nova Square', 'nova_square'), ('Numans', 'numans'), ('Nunito', 'nunito'), ('Nunito Sans', 'nunito_sans'), ('Odor Mean Chey', 'odor_mean_chey'), ('Offside', 'offside'), ('Old Standard TT', 'old_standard_tt'), ('Oldenburg', 'oldenburg'), ('Oleo Script', 'oleo_script'), ('Oleo Script Swash Caps', 'oleo_script_swash_caps'), ('Open Sans', 'open_sans'), ('Open Sans Condensed', 'open_sans_condensed'), ('Oranienbaum', 'oranienbaum'), ('Orbitron', 'orbitron'), ('Oregano', 'oregano'), ('Orienta', 'orienta'), ('Original Surfer', 'original_surfer'), ('Oswald', 'oswald'), ('Over the Rainbow', 'over_the_rainbow'), ('Overlock', 'overlock'), ('Overlock SC', 'overlock_sc'), ('Overpass', 'overpass'), ('Overpass Mono', 'overpass_mono'), ('Ovo', 'ovo'), ('Oxygen', 'oxygen'), ('Oxygen Mono', 'oxygen_mono'), ('PT Mono', 'pt_mono'), ('PT Sans', 'pt_sans'), ('PT Sans Caption', 'pt_sans_caption'), ('PT Sans Narrow', 'pt_sans_narrow'), ('PT Serif', 'pt_serif'), ('PT Serif Caption', 'pt_serif_caption'), ('Pacifico', 'pacifico'), ('Padauk', 'padauk'), ('Palanquin', 'palanquin'), ('Palanquin Dark', 'palanquin_dark'), ('Pangolin', 'pangolin'), ('Paprika', 'paprika'), ('Parisienne', 'parisienne'), ('Passero One', 'passero_one'), ('Passion One', 'passion_one'), ('Pathway Gothic One', 'pathway_gothic_one'), ('Patrick Hand', 'patrick_hand'), ('Patrick Hand SC', 'patrick_hand_sc'), ('Pattaya', 'pattaya'), ('Patua One', 'patua_one'), ('Pavanam', 'pavanam'), ('Paytone One', 'paytone_one'), ('Peddana', 'peddana'), ('Peralta', 'peralta'), ('Permanent Marker', 'permanent_marker'), ('Petit Formal Script', 'petit_formal_script'), ('Petrona', 'petrona'), ('Philosopher', 'philosopher'), ('Piedra', 'piedra'), ('Pinyon Script', 'pinyon_script'), ('Pirata One', 'pirata_one'), ('Plaster', 'plaster'), ('Play', 'play'), ('Playball', 'playball'), ('Playfair Display', 'playfair_display'), ('Playfair Display SC', 'playfair_display_sc'), ('Podkova', 'podkova'), ('Poiret One', 'poiret_one'), ('Poller One', 'poller_one'), ('Poly', 'poly'), ('Pompiere', 'pompiere'), ('Pontano Sans', 'pontano_sans'), ('Poppins', 'poppins'), ('Port Lligat Sans', 'port_lligat_sans'), ('Port Lligat Slab', 'port_lligat_slab'), ('Pragati Narrow', 'pragati_narrow'), ('Prata', 'prata'), ('Preahvihear', 'preahvihear'), ('Press Start 2P', 'press_start_2p'), ('Pridi', 'pridi'), ('Princess Sofia', 'princess_sofia'), ('Prociono', 'prociono'), ('Prompt', 'prompt'), ('Prosto One', 'prosto_one'), ('Proza Libre', 'proza_libre'), ('Puritan', 'puritan'), ('Purple Purse', 'purple_purse'), ('Quando', 'quando'), ('Quantico', 'quantico'), ('Quattrocento', 'quattrocento'), ('Quattrocento Sans', 'quattrocento_sans'), ('Questrial', 'questrial'), ('Quicksand', 'quicksand'), ('Quintessential', 'quintessential'), ('Qwigley', 'qwigley'), ('Racing Sans One', 'racing_sans_one'), ('Radley', 'radley'), ('Rajdhani', 'rajdhani'), ('Rakkas', 'rakkas'), ('Raleway', 'raleway'), ('Raleway Dots', 'raleway_dots'), ('Ramabhadra', 'ramabhadra'), ('Ramaraja', 'ramaraja'), ('Rambla', 'rambla'), ('Rammetto One', 'rammetto_one'), ('Ranchers', 'ranchers'), ('Rancho', 'rancho'), ('Ranga', 'ranga'), ('Rasa', 'rasa'), ('Rationale', 'rationale'), ('Ravi Prakash', 'ravi_prakash'), ('Redressed', 'redressed'), ('Reem Kufi', 'reem_kufi'), ('Reenie Beanie', 'reenie_beanie'), ('Revalia', 'revalia'), ('Rhodium Libre', 'rhodium_libre'), ('Ribeye', 'ribeye'), ('Ribeye Marrow', 'ribeye_marrow'), ('Righteous', 'righteous'), ('Risque', 'risque'), ('Roboto', 'roboto'), ('Roboto Condensed', 'roboto_condensed'), ('Roboto Mono', 'roboto_mono'), ('Roboto Slab', 'roboto_slab'), ('Rochester', 'rochester'), ('Rock Salt', 'rock_salt'), ('Rokkitt', 'rokkitt'), ('Romanesco', 'romanesco'), ('Ropa Sans', 'ropa_sans'), ('Rosario', 'rosario'), ('Rosarivo', 'rosarivo'), ('Rouge Script', 'rouge_script'), ('Rozha One', 'rozha_one'), ('Rubik', 'rubik'), ('Rubik Mono One', 'rubik_mono_one'), ('Ruda', 'ruda'), ('Rufina', 'rufina'), ('Ruge Boogie', 'ruge_boogie'), ('Ruluko', 'ruluko'), ('Rum Raisin', 'rum_raisin'), ('Ruslan Display', 'ruslan_display'), ('Russo One', 'russo_one'), ('Ruthie', 'ruthie'), ('Rye', 'rye'), ('Sacramento', 'sacramento'), ('Sahitya', 'sahitya'), ('Sail', 'sail'), ('Saira', 'saira'), ('Saira Condensed', 'saira_condensed'), ('Saira Extra Condensed', 'saira_extra_condensed'), ('Saira Semi Condensed', 'saira_semi_condensed'), ('Salsa', 'salsa'), ('Sanchez', 'sanchez'), ('Sancreek', 'sancreek'), ('Sansita', 'sansita'), ('Sarala', 'sarala'), ('Sarina', 'sarina'), ('Sarpanch', 'sarpanch'), ('Satisfy', 'satisfy'), ('Scada', 'scada'), ('Scheherazade', 'scheherazade'), ('Schoolbell', 'schoolbell'), ('Scope One', 'scope_one'), ('Seaweed Script', 'seaweed_script'), ('Secular One', 'secular_one'), ('Sedgwick Ave', 'sedgwick_ave'), ('Sedgwick Ave Display', 'sedgwick_ave_display'), ('Sevillana', 'sevillana'), ('Seymour One', 'seymour_one'), ('Shadows Into Light', 'shadows_into_light'), ('Shadows Into Light Two', 'shadows_into_light_two'), ('Shanti', 'shanti'), ('Share', 'share'), ('Share Tech', 'share_tech'), ('Share Tech Mono', 'share_tech_mono'), ('Shojumaru', 'shojumaru'), ('Short Stack', 'short_stack'), ('Shrikhand', 'shrikhand'), ('Siemreap', 'siemreap'), ('Sigmar One', 'sigmar_one'), ('Signika', 'signika'), ('Signika Negative', 'signika_negative'), ('Simonetta', 'simonetta'), ('Sintony', 'sintony'), ('Sirin Stencil', 'sirin_stencil'), ('Six Caps', 'six_caps'), ('Skranji', 'skranji'), ('Slabo 13px', 'slabo_13px'), ('Slabo 27px', 'slabo_27px'), ('Slackey', 'slackey'), ('Smokum', 'smokum'), ('Smythe', 'smythe'), ('Sniglet', 'sniglet'), ('Snippet', 'snippet'), ('Snowburst One', 'snowburst_one'), ('Sofadi One', 'sofadi_one'), ('Sofia', 'sofia'), ('Sonsie One', 'sonsie_one'), ('Sorts Mill Goudy', 'sorts_mill_goudy'), ('Source Code Pro', 'source_code_pro'), ('Source Sans Pro', 'source_sans_pro'), ('Source Serif Pro', 'source_serif_pro'), ('Space Mono', 'space_mono'), ('Special Elite', 'special_elite'), ('Spectral', 'spectral'), ('Spectral SC', 'spectral_sc'), ('Spicy Rice', 'spicy_rice'), ('Spinnaker', 'spinnaker'), ('Spirax', 'spirax'), ('Squada One', 'squada_one'), ('Sree Krushnadevaraya', 'sree_krushnadevaraya'), ('Sriracha', 'sriracha'), ('Stalemate', 'stalemate'), ('Stalinist One', 'stalinist_one'), ('Stardos Stencil', 'stardos_stencil'), ('Stint Ultra Condensed', 'stint_ultra_condensed'), ('Stint Ultra Expanded', 'stint_ultra_expanded'), ('Stoke', 'stoke'), ('Strait', 'strait'), ('Sue Ellen Francisco', 'sue_ellen_francisco'), ('Suez One', 'suez_one'), ('Sumana', 'sumana'), ('Sunshiney', 'sunshiney'), ('Supermercado One', 'supermercado_one'), ('Sura', 'sura'), ('Suranna', 'suranna'), ('Suravaram', 'suravaram'), ('Suwannaphum', 'suwannaphum'), ('Swanky and Moo Moo', 'swanky_and_moo_moo'), ('Syncopate', 'syncopate'), ('Tangerine', 'tangerine'), ('Taprom', 'taprom'), ('Tauri', 'tauri'), ('Taviraj', 'taviraj'), ('Teko', 'teko'), ('Telex', 'telex'), ('Tenali Ramakrishna', 'tenali_ramakrishna'), ('Tenor Sans', 'tenor_sans'), ('Text Me One', 'text_me_one'), ('The Girl Next Door', 'the_girl_next_door'), ('Tienne', 'tienne'), ('Tillana', 'tillana'), ('Timmana', 'timmana'), ('Tinos', 'tinos'), ('Titan One', 'titan_one'), ('Titillium Web', 'titillium_web'), ('Trade Winds', 'trade_winds'), ('Trirong', 'trirong'), ('Trocchi', 'trocchi'), ('Trochut', 'trochut'), ('Trykker', 'trykker'), ('Tulpen One', 'tulpen_one'), ('Ubuntu', 'ubuntu'), ('Ubuntu Condensed', 'ubuntu_condensed'), ('Ubuntu Mono', 'ubuntu_mono'), ('Ultra', 'ultra'), ('Uncial Antiqua', 'uncial_antiqua'), ('Underdog', 'underdog'), ('Unica One', 'unica_one'), ('UnifrakturCook', 'unifrakturcook'), ('UnifrakturMaguntia', 'unifrakturmaguntia'), ('Unkempt', 'unkempt'), ('Unlock', 'unlock'), ('Unna', 'unna'), ('VT323', 'vt323'), ('Vampiro One', 'vampiro_one'), ('Varela', 'varela'), ('Varela Round', 'varela_round'), ('Vast Shadow', 'vast_shadow'), ('Vesper Libre', 'vesper_libre'), ('Vibur', 'vibur'), ('Vidaloka', 'vidaloka'), ('Viga', 'viga'), ('Voces', 'voces'), ('Volkhov', 'volkhov'), ('Vollkorn', 'vollkorn'), ('Vollkorn SC', 'vollkorn_sc'), ('Voltaire', 'voltaire'), ('Waiting for the Sunrise', 'waiting_for_the_sunrise'), ('Wallpoet', 'wallpoet'), ('Walter Turncoat', 'walter_turncoat'), ('Warnes', 'warnes'), ('Wellfleet', 'wellfleet'), ('Wendy One', 'wendy_one'), ('Wire One', 'wire_one'), ('Work Sans', 'work_sans'), ('Yanone Kaffeesatz', 'yanone_kaffeesatz'), ('Yantramanav', 'yantramanav'), ('Yatra One', 'yatra_one'), ('Yellowtail', 'yellowtail'), ('Yeseva One', 'yeseva_one'), ('Yesteryear', 'yesteryear'), ('Yrsa', 'yrsa'), ('Zeyada', 'zeyada'), ('Zilla Slab', 'zilla_slab'), ('Zilla Slab Highlight', 'zilla_slab_highlight'), ('Proxima Nova', 'proxima_nova'), ('Baskerville', 'baskerville'), ('Chunk Five', 'chunk_five'), ('League Gothic', 'league_gothic'), ('Trajan', 'trajan'), ('Franchise', 'franchise'), ('Harriet', 'harriet'), ('Larish Neue', 'larish_neue'), ('Ogg', 'ogg'), ('Domaine Display', 'domaine_display'), ('Transcript', 'transcript'), ('Opposit', 'opposit'), ('Moniker', 'moniker'), ('Trade Gothic Display', 'trade_gothic_display'), ('Mont', 'mont'), ('Noe Display', 'noe_display'), ('Futura PT', 'futura_pt'), ('Museo Sans', 'museo_sans'), ('Museo Slab', 'museo_slab'), ('Adelle', 'adelle'), ('Brandon Grotesque', 'brandon_grotesque'), ('Nimbus Sans', 'nimbus_sans'), ('Myriad Pro', 'myriad_pro'), ('Freight Sans Pro', 'freight_sans_pro'), ('FF Tisa Pro', 'ff_tisa_pro'), ('Museo', 'museo'), ('JAF Facit', 'jaf_facit'), ('Omnes Pro', 'omnes_pro'), ('FF Enzo', 'ff_enzo'), ('Chaparral Pro', 'chaparral_pro'), ('FF Meta Serif Pro', 'ff_meta_serif_pro'), ('FF Meta Pro', 'ff_meta_pro'), ('FF Dagny Pro', 'ff_dagny_pro'), ('Jubilat', 'jubilat'), ('League Gothic', 'league_gothic'), ('Adobe Garamond Pro', 'adobe_garamond_pro'), ('Adelle Sans', 'adelle_sans'), ('Minion Pro', 'minion_pro'), ('FF Market Pro', 'ff_market_pro'), ('Garamond', 'garamond'), ('Helvetica', 'helvetica'), ('Trajan', 'trajan'), ('Futura', 'futura'), ('Bodoni', 'bodoni'), ('Zorus Serif', 'zorus_serif'), ('Sabo', 'sabo'), ('Bobber', 'bobber'), ('Akura Popo', 'akura_popo'), ('Berlin', 'berlin'), ('Rockwell', 'rockwell'), ('Didot', 'didot'), ('Univers', 'univers'), ('ITC Lubalin Graph', 'itc_lubalin_graph'), ('Frutiger', 'frutiger'), ('ITC Bauhaus', 'itc_bauhaus'), ('FF Meta', 'ff_meta'), ('FF Blur', 'ff_blur'), ('Horizon', 'horizon'), ('Big Caslon', 'big_caslon'), ('Sackers Gothic', 'sackers_gothic'), ('FF Din', 'ff_din'), ('Sassoon', 'sassoon'), ('Baltica-2', 'baltica-2'), ('FF Avance', 'ff_avance'), ('Modesto', 'modesto'), ('Neo Sans', 'neo_sans'), ('Proxima Nova', 'proxima_nova'), ('Foco', 'foco'), ('Tondo', 'tondo'), ('Museo Sans3', 'museo_sans3'), ('Uni Sans', 'uni_sans'), ('Neue Swift', 'neue_swift'), ('Brandon Grotesque', 'brandon_grotesque'), ('Bodoni Egyptian Pro', 'bodoni_egyptian_pro'), ('Revista', 'revista'), ('Bambusa Pro', 'bambusa_pro'), ('Amsi Pro', 'amsi_pro'), ('Aventura', 'aventura'), ('Axis', 'axis'), ('Azedo', 'azedo'), ('Elegant Lux Pro3', 'elegant_lux_pro3'), ('Futuracha', 'futuracha'), ('Building', 'building'), ('Canilari', 'canilari'), ('Posterama', 'posterama'), ('Grenale Slab', 'grenale_slab'), ('Docu', 'docu'), ('Rufina', 'rufina')], max_length=64, null=True),
        ),
    ]
