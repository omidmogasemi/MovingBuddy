import ListItem from "components/list-item";
import { Grid, Container, Text } from 'theme-ui'; 

const data = [
    {}, {}, {} 
]

export default function ListContent() { 
    return ( 
        <section sx={{variant: 'section.listContent'}} id="list-content">
            <Container> 
                <Grid sx={styles.grid}> 
                    {data.map((item, i) => ( 
                        <Container sx={styles.container} key={i}>
                            <Text as="h3" sx={{...styles.header_text, variant: "spans.primary"}}>Living Room</Text>
                            <ListItem /> 
                        </Container>
                    ))}
                </Grid> 
            </Container> 
        </section>
    );
}

const styles = {
    grid: {
        width: '100%', 
        mx: 'auto',
        gridGap: [
            '35px 0',
            null,
            '40px 40px',
            '50px 60px',
            '30px',
            '50px 40px',
            '55px 90px',
        ],
        gridTemplateColumns: [
            'repeat(1,1fr)',
            null,
            'repeat(2,1fr)',
        ],
    },
    header_text: { 
        mb: 2,
    }, 
    container: { 
        width: '370px', 
    }, 
};